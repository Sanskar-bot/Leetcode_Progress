# =============================================================
#  LeetCode Progress Tracker — Daily Update Script
#  Fetches latest data from LeetCode API and pushes to GitHub
#  Repo: https://github.com/Sanskar-bot/Leetcode_Progress
# =============================================================

$REPO_DIR   = "C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode"
$USERNAME   = "Sanskar_phougat"
$TIMESTAMP  = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$DATE       = Get-Date -Format "yyyy-MM-dd"

Write-Host "`n🔄 Fetching LeetCode data for $USERNAME..." -ForegroundColor Cyan

# ── 1. Fetch overall stats ────────────────────────────────────
$statsBody = '{"query":"{ matchedUser(username: \"' + $USERNAME + '\") { username profile { realName ranking } submitStats { acSubmissionNum { difficulty count submissions } } } }"}'
$statsResp = Invoke-RestMethod -Uri "https://leetcode.com/graphql" -Method POST -ContentType "application/json" -Body $statsBody
$user      = $statsResp.data.matchedUser
$acNums    = $user.submitStats.acSubmissionNum

$totalSolved      = ($acNums | Where-Object { $_.difficulty -eq "All"    }).count
$totalSubmissions = ($acNums | Where-Object { $_.difficulty -eq "All"    }).submissions
$easySolved       = ($acNums | Where-Object { $_.difficulty -eq "Easy"   }).count
$easySubs         = ($acNums | Where-Object { $_.difficulty -eq "Easy"   }).submissions
$mediumSolved     = ($acNums | Where-Object { $_.difficulty -eq "Medium" }).count
$mediumSubs       = ($acNums | Where-Object { $_.difficulty -eq "Medium" }).submissions
$hardSolved       = ($acNums | Where-Object { $_.difficulty -eq "Hard"   }).count
$hardSubs         = ($acNums | Where-Object { $_.difficulty -eq "Hard"   }).submissions
$ranking          = $user.profile.ranking

Write-Host "  ✅ Stats: $totalSolved solved (E:$easySolved M:$mediumSolved H:$hardSolved) | Rank: $ranking" -ForegroundColor Green

# ── 2. Fetch topic tag breakdown ─────────────────────────────
$tagsBody = '{"query":"{ matchedUser(username: \"' + $USERNAME + '\") { tagProblemCounts { advanced { tagName tagSlug problemsSolved } intermediate { tagName tagSlug problemsSolved } fundamental { tagName tagSlug problemsSolved } } } }"}'
$tagsResp = Invoke-RestMethod -Uri "https://leetcode.com/graphql" -Method POST -ContentType "application/json" -Body $tagsBody
$tags     = $tagsResp.data.matchedUser.tagProblemCounts

Write-Host "  ✅ Topics fetched" -ForegroundColor Green

# ── 3. Fetch recent accepted submissions ─────────────────────
$recentBody = '{"query":"{ recentAcSubmissionList(username: \"' + $USERNAME + '\", limit: 50) { id title titleSlug timestamp } }"}'
$recentResp = Invoke-RestMethod -Uri "https://leetcode.com/graphql" -Method POST -ContentType "application/json" -Body $recentBody
$submissions = $recentResp.data.recentAcSubmissionList

$recentList = $submissions | ForEach-Object {
    $dt = [DateTimeOffset]::FromUnixTimeSeconds([long]$_.timestamp).ToLocalTime().ToString("yyyy-MM-dd")
    [PSCustomObject]@{ title = $_.title; slug = $_.titleSlug; date = $dt }
}
Write-Host "  ✅ Recent submissions: $($recentList.Count) fetched" -ForegroundColor Green

# ── 4. Build JSON dataset ─────────────────────────────────────
$data = [ordered]@{
    meta = [ordered]@{
        username     = $USERNAME
        profile_url  = "https://leetcode.com/u/$USERNAME/"
        last_updated = $TIMESTAMP
    }
    stats = [ordered]@{
        ranking           = $ranking
        total_solved      = $totalSolved
        total_submissions = $totalSubmissions
        by_difficulty     = [ordered]@{
            Easy   = [ordered]@{ solved = $easySolved;  submissions = $easySubs   }
            Medium = [ordered]@{ solved = $mediumSolved; submissions = $mediumSubs }
            Hard   = [ordered]@{ solved = $hardSolved;  submissions = $hardSubs   }
        }
    }
    topics = [ordered]@{
        fundamental  = $tags.fundamental  | ForEach-Object { [ordered]@{ tag = $_.tagName; solved = $_.problemsSolved } }
        intermediate = $tags.intermediate | ForEach-Object { [ordered]@{ tag = $_.tagName; solved = $_.problemsSolved } }
        advanced     = $tags.advanced     | ForEach-Object { [ordered]@{ tag = $_.tagName; solved = $_.problemsSolved } }
    }
    recent_accepted_submissions = $recentList
}

$jsonOut = $data | ConvertTo-Json -Depth 10
Set-Content -Path "$REPO_DIR\progress_tracker.json" -Value $jsonOut -Encoding UTF8
Write-Host "  ✅ progress_tracker.json updated" -ForegroundColor Green

# ── 5. Rebuild README.md ──────────────────────────────────────
$acceptanceRate = if ($totalSubmissions -gt 0) { [math]::Round(($totalSolved / $totalSubmissions) * 100) } else { 0 }

$recentTable = ""
$i = 1
foreach ($s in $recentList) {
    $url = "https://leetcode.com/problems/$($s.slug)/"
    $recentTable += "| $i | [$($s.title)]($url) | $($s.date) |`n"
    $i++
}

$fundamentalTable  = ($tags.fundamental  | ForEach-Object { "| $($_.tagName) | $($_.problemsSolved) |" }) -join "`n"
$intermediateTable = ($tags.intermediate | ForEach-Object { "| $($_.tagName) | $($_.problemsSolved) |" }) -join "`n"
$advancedTable     = ($tags.advanced     | ForEach-Object { "| $($_.tagName) | $($_.problemsSolved) |" }) -join "`n"

$readme = @"
# 🧑‍💻 Sanskar's LeetCode Progress Tracker

> Auto-updated daily via GitHub push • Profile: [Sanskar_phougat](https://leetcode.com/u/Sanskar_phougat/)

---

## 📊 Overall Stats

| Metric | Value |
|---|---|
| 🏆 Global Ranking | #$("{0:N0}" -f $ranking) |
| ✅ Total Solved | **$totalSolved** problems |
| 📬 Total Submissions | $totalSubmissions |
| 🎯 Acceptance Rate | ~$acceptanceRate% |

### Difficulty Breakdown

| 🟢 Easy | 🟡 Medium | 🔴 Hard |
|---|---|---|
| $easySolved | $mediumSolved | $hardSolved |

---

## 🏷️ Topics Covered

### 🟦 Fundamental
| Topic | Solved |
|---|---|
$fundamentalTable

### 🟨 Intermediate
| Topic | Solved |
|---|---|
$intermediateTable

### 🟥 Advanced
| Topic | Solved |
|---|---|
$advancedTable

---

## 🕒 Recent Accepted Submissions

| # | Problem | Date |
|---|---|---|
$recentTable
---

## 📁 Files in this repo

| File | Description |
|---|---|
| ``progress_tracker.json`` | Raw data — all stats, topics, submissions |
| ``README.md`` | This file — auto-updated daily |
| ``update_progress.ps1`` | Script that fetches data and pushes to GitHub |

---

*Last updated: $TIMESTAMP • Auto-pushed by Antigravity agent*
"@

Set-Content -Path "$REPO_DIR\README.md" -Value $readme -Encoding UTF8
Write-Host "  ✅ README.md rebuilt" -ForegroundColor Green

# ── 6. Git commit & push ──────────────────────────────────────
Set-Location $REPO_DIR
git add progress_tracker.json README.md
$commitMsg = "📊 Daily update: $totalSolved solved (E:$easySolved M:$mediumSolved H:$hardSolved) [$DATE]"
git commit -m $commitMsg
git push origin main

Write-Host "`n🚀 Pushed to GitHub successfully!" -ForegroundColor Green
Write-Host "   → https://github.com/Sanskar-bot/Leetcode_Progress`n" -ForegroundColor Cyan
