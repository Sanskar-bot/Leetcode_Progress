# ============================================================
#  LeetCode Tracker — Modern Windows 11 Style Popup
#  Called by startup_prompt.vbs on login
# ============================================================

Add-Type -AssemblyName PresentationFramework
Add-Type -AssemblyName PresentationCore
Add-Type -AssemblyName WindowsBase
Add-Type -AssemblyName System.Windows.Forms

# ── Load current stats from JSON ─────────────────────────────
$jsonPath = "C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode\progress_tracker.json"
$totalSolved = "?"; $easySolved = "?"; $mediumSolved = "?"; $hardSolved = "?"; $lastUpdated = "Never"

if (Test-Path $jsonPath) {
    try {
        $data        = Get-Content $jsonPath -Raw | ConvertFrom-Json
        $totalSolved   = $data.stats.total_solved
        $easySolved    = $data.stats.by_difficulty.Easy.solved
        $mediumSolved  = $data.stats.by_difficulty.Medium.solved
        $hardSolved    = $data.stats.by_difficulty.Hard.solved
        $lastUpdated   = $data.meta.last_updated.ToString().Substring(0,10)
    } catch {}
}

# ── XAML Layout ──────────────────────────────────────────────
[xml]$xaml = @"
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="LeetCode Tracker"
    Width="420" Height="320"
    WindowStartupLocation="CenterScreen"
    ResizeMode="NoResize"
    WindowStyle="None"
    AllowsTransparency="True"
    Background="Transparent"
    Topmost="True">

  <Window.Resources>
    <Style x:Key="PrimaryBtn" TargetType="Button">
      <Setter Property="Background" Value="#F89F1B"/>
      <Setter Property="Foreground" Value="#0D0D0D"/>
      <Setter Property="FontFamily" Value="Segoe UI Variable Display, Segoe UI"/>
      <Setter Property="FontSize" Value="13"/>
      <Setter Property="FontWeight" Value="SemiBold"/>
      <Setter Property="Height" Value="38"/>
      <Setter Property="Width" Value="150"/>
      <Setter Property="Cursor" Value="Hand"/>
      <Setter Property="BorderThickness" Value="0"/>
      <Setter Property="Template">
        <Setter.Value>
          <ControlTemplate TargetType="Button">
            <Border Background="{TemplateBinding Background}" CornerRadius="8" Padding="12,0">
              <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Border>
            <ControlTemplate.Triggers>
              <Trigger Property="IsMouseOver" Value="True">
                <Setter Property="Background" Value="#FFBA42"/>
              </Trigger>
              <Trigger Property="IsPressed" Value="True">
                <Setter Property="Background" Value="#D4860E"/>
              </Trigger>
            </ControlTemplate.Triggers>
          </ControlTemplate>
        </Setter.Value>
      </Setter>
    </Style>
    <Style x:Key="SecondaryBtn" TargetType="Button">
      <Setter Property="Background" Value="#2A2A2A"/>
      <Setter Property="Foreground" Value="#AAAAAA"/>
      <Setter Property="FontFamily" Value="Segoe UI Variable Display, Segoe UI"/>
      <Setter Property="FontSize" Value="13"/>
      <Setter Property="FontWeight" Value="SemiBold"/>
      <Setter Property="Height" Value="38"/>
      <Setter Property="Width" Value="150"/>
      <Setter Property="Cursor" Value="Hand"/>
      <Setter Property="BorderThickness" Value="0"/>
      <Setter Property="Template">
        <Setter.Value>
          <ControlTemplate TargetType="Button">
            <Border Background="{TemplateBinding Background}" CornerRadius="8" Padding="12,0">
              <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Border>
            <ControlTemplate.Triggers>
              <Trigger Property="IsMouseOver" Value="True">
                <Setter Property="Background" Value="#333333"/>
              </Trigger>
              <Trigger Property="IsPressed" Value="True">
                <Setter Property="Background" Value="#1E1E1E"/>
              </Trigger>
            </ControlTemplate.Triggers>
          </ControlTemplate>
        </Setter.Value>
      </Setter>
    </Style>
  </Window.Resources>

  <Border Background="#1A1A1A" CornerRadius="16" Margin="10">
    <Border.Effect>
      <DropShadowEffect BlurRadius="30" ShadowDepth="6" Opacity="0.6" Color="#000000"/>
    </Border.Effect>

    <Grid>
      <Grid.RowDefinitions>
        <RowDefinition Height="Auto"/>
        <RowDefinition Height="*"/>
        <RowDefinition Height="Auto"/>
        <RowDefinition Height="Auto"/>
      </Grid.RowDefinitions>

      <!-- Drag bar -->
      <Border Grid.Row="0" Background="Transparent" Height="32" x:Name="DragBar"/>

      <!-- Close button -->
      <Button Grid.Row="0" Content="✕" HorizontalAlignment="Right" VerticalAlignment="Center"
              Margin="0,0,14,0" Width="28" Height="28" FontSize="11"
              Background="Transparent" Foreground="#666666" BorderThickness="0"
              Cursor="Hand" x:Name="CloseBtn">
        <Button.Template>
          <ControlTemplate TargetType="Button">
            <Border Background="{TemplateBinding Background}" CornerRadius="6">
              <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Border>
            <ControlTemplate.Triggers>
              <Trigger Property="IsMouseOver" Value="True">
                <Setter Property="Background" Value="#3A3A3A"/>
                <Setter Property="Foreground" Value="#FFFFFF"/>
              </Trigger>
            </ControlTemplate.Triggers>
          </ControlTemplate>
        </Button.Template>
      </Button>

      <!-- Main content -->
      <StackPanel Grid.Row="1" Margin="28,0,28,0" VerticalAlignment="Center">

        <!-- Icon + Title -->
        <StackPanel Orientation="Horizontal" Margin="0,0,0,6">
          <TextBlock Text="&#x1F9E9;" FontSize="26" VerticalAlignment="Center" Margin="0,0,10,0"/>
          <StackPanel VerticalAlignment="Center">
            <TextBlock Text="LeetCode Tracker" FontFamily="Segoe UI Variable Display, Segoe UI"
                       FontSize="17" FontWeight="Bold" Foreground="#FFFFFF"/>
            <TextBlock Text="Daily Progress Sync" FontFamily="Segoe UI, Segoe UI"
                       FontSize="11" Foreground="#666666"/>
          </StackPanel>
        </StackPanel>

        <!-- Divider -->
        <Border Height="1" Background="#2A2A2A" Margin="0,10,0,14"/>

        <!-- Stats Row -->
        <Grid Margin="0,0,0,14">
          <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="*"/>
          </Grid.ColumnDefinitions>

          <!-- Total -->
          <Border Grid.Column="0" Background="#242424" CornerRadius="10" Padding="8,10" Margin="0,0,5,0">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="TOTAL" FontSize="9" FontWeight="Bold" Foreground="#555555"
                         HorizontalAlignment="Center" FontFamily="Segoe UI"/>
              <TextBlock x:Name="TotalText" FontSize="22" FontWeight="Bold" Foreground="#FFFFFF"
                         HorizontalAlignment="Center" FontFamily="Segoe UI Variable Display, Segoe UI"/>
            </StackPanel>
          </Border>
          <!-- Easy -->
          <Border Grid.Column="1" Background="#1A2E1A" CornerRadius="10" Padding="8,10" Margin="0,0,5,0">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="EASY" FontSize="9" FontWeight="Bold" Foreground="#3D7A3D"
                         HorizontalAlignment="Center" FontFamily="Segoe UI"/>
              <TextBlock x:Name="EasyText" FontSize="22" FontWeight="Bold" Foreground="#4EC94E"
                         HorizontalAlignment="Center" FontFamily="Segoe UI Variable Display, Segoe UI"/>
            </StackPanel>
          </Border>
          <!-- Medium -->
          <Border Grid.Column="2" Background="#2E2510" CornerRadius="10" Padding="8,10" Margin="0,0,5,0">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="MED" FontSize="9" FontWeight="Bold" Foreground="#7A6020"
                         HorizontalAlignment="Center" FontFamily="Segoe UI"/>
              <TextBlock x:Name="MediumText" FontSize="22" FontWeight="Bold" Foreground="#F89F1B"
                         HorizontalAlignment="Center" FontFamily="Segoe UI Variable Display, Segoe UI"/>
            </StackPanel>
          </Border>
          <!-- Hard -->
          <Border Grid.Column="3" Background="#2E1A1A" CornerRadius="10" Padding="8,10">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="HARD" FontSize="9" FontWeight="Bold" Foreground="#7A3D3D"
                         HorizontalAlignment="Center" FontFamily="Segoe UI"/>
              <TextBlock x:Name="HardText" FontSize="22" FontWeight="Bold" Foreground="#FF6B6B"
                         HorizontalAlignment="Center" FontFamily="Segoe UI Variable Display, Segoe UI"/>
            </StackPanel>
          </Border>
        </Grid>

        <!-- Last updated -->
        <TextBlock x:Name="LastUpdatedText" FontSize="11" Foreground="#444444"
                   HorizontalAlignment="Center" FontFamily="Segoe UI" Margin="0,0,0,4"/>
      </StackPanel>

      <!-- Divider -->
      <Border Grid.Row="2" Height="1" Background="#242424" Margin="0,0,0,0"/>

      <!-- Buttons -->
      <StackPanel Grid.Row="3" Orientation="Horizontal" HorizontalAlignment="Center"
                  Margin="0,16,0,22">
        <Button x:Name="YesBtn" Style="{StaticResource PrimaryBtn}" Content="⬆  Sync Now" Margin="0,0,12,0"/>
        <Button x:Name="NoBtn"  Style="{StaticResource SecondaryBtn}" Content="Skip for now"/>
      </StackPanel>

    </Grid>
  </Border>
</Window>
"@

# ── Build Window ──────────────────────────────────────────────
$reader = New-Object System.Xml.XmlNodeReader $xaml
$window = [Windows.Markup.XamlReader]::Load($reader)

# Fill in live stats
$window.FindName("TotalText").Text      = "$totalSolved"
$window.FindName("EasyText").Text       = "$easySolved"
$window.FindName("MediumText").Text     = "$mediumSolved"
$window.FindName("HardText").Text       = "$hardSolved"
$window.FindName("LastUpdatedText").Text = "Last synced: $lastUpdated"

# ── Wire up drag ──────────────────────────────────────────────
$dragBar = $window.FindName("DragBar")
$dragBar.Add_MouseLeftButtonDown({ $window.DragMove() })

# ── Wire up buttons ───────────────────────────────────────────
$result = $false

$window.FindName("YesBtn").Add_Click({
    $script:result = $true
    $window.Close()
})
$window.FindName("NoBtn").Add_Click({
    $script:result = $false
    $window.Close()
})
$window.FindName("CloseBtn").Add_Click({
    $script:result = $false
    $window.Close()
})

$window.ShowDialog() | Out-Null

# ── Run updater if Yes ────────────────────────────────────────
if ($result) {
    Start-Process powershell.exe -ArgumentList "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode\update_progress.ps1`"" -WindowStyle Hidden

    # Show a brief toast-style confirmation
    [xml]$toastXaml = @"
<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        Width="320" Height="70" WindowStartupLocation="Manual"
        ResizeMode="NoResize" WindowStyle="None" AllowsTransparency="True"
        Background="Transparent" Topmost="True">
  <Border Background="#1A1A1A" CornerRadius="12" Margin="6">
    <Border.Effect>
      <DropShadowEffect BlurRadius="20" ShadowDepth="4" Opacity="0.5" Color="#000000"/>
    </Border.Effect>
    <StackPanel Orientation="Horizontal" VerticalAlignment="Center" Margin="16,0">
      <TextBlock Text="✅" FontSize="20" VerticalAlignment="Center" Margin="0,0,12,0"/>
      <StackPanel VerticalAlignment="Center">
        <TextBlock Text="Syncing to GitHub..." FontFamily="Segoe UI Variable Display, Segoe UI"
                   FontSize="13" FontWeight="SemiBold" Foreground="#FFFFFF"/>
        <TextBlock Text="LeetCode progress update running in background"
                   FontFamily="Segoe UI" FontSize="10" Foreground="#666666"/>
      </StackPanel>
    </StackPanel>
  </Border>
</Window>
"@
    $toastReader = New-Object System.Xml.XmlNodeReader $toastXaml
    $toast = [Windows.Markup.XamlReader]::Load($toastReader)

    # Position bottom-right corner
    $screen = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
    $toast.Left = $screen.Right - 340
    $toast.Top  = $screen.Bottom - 90

    $toast.Show()
    Start-Sleep -Seconds 3
    $toast.Close()
}
