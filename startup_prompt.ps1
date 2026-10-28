# ============================================================
#  LeetCode Tracker - Modern Windows 11 Style Popup
#  Clean formal design, no emojis
# ============================================================

Add-Type -AssemblyName PresentationFramework
Add-Type -AssemblyName PresentationCore
Add-Type -AssemblyName WindowsBase
Add-Type -AssemblyName System.Windows.Forms

# -- Load current stats from JSON -----------------------------
$jsonPath    = "C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode\progress_tracker.json"
$totalSolved  = "--"; $easySolved = "--"; $mediumSolved = "--"; $hardSolved = "--"
$lastUpdated  = "Never synced"

if (Test-Path $jsonPath) {
    try {
        $data         = Get-Content $jsonPath -Raw | ConvertFrom-Json
        $totalSolved  = $data.stats.total_solved
        $easySolved   = $data.stats.by_difficulty.Easy.solved
        $mediumSolved = $data.stats.by_difficulty.Medium.solved
        $hardSolved   = $data.stats.by_difficulty.Hard.solved
        $lastUpdated  = "Last synced  " + $data.meta.last_updated.ToString().Substring(0,10)
    } catch {}
}

# -- XAML -----------------------------------------------------
[xml]$xaml = @"
<Window
    xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
    xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml"
    Title="LeetCode Tracker"
    Width="400" Height="290"
    WindowStartupLocation="CenterScreen"
    ResizeMode="NoResize"
    WindowStyle="None"
    AllowsTransparency="True"
    Background="Transparent"
    Topmost="True">

  <Window.Resources>

    <!-- Primary (Sync) button -->
    <Style x:Key="PrimaryBtn" TargetType="Button">
      <Setter Property="Background"   Value="#F5A623"/>
      <Setter Property="Foreground"   Value="#0D0D0D"/>
      <Setter Property="FontFamily"   Value="Segoe UI Variable Display, Segoe UI"/>
      <Setter Property="FontSize"     Value="13"/>
      <Setter Property="FontWeight"   Value="SemiBold"/>
      <Setter Property="Height"       Value="36"/>
      <Setter Property="Width"        Value="148"/>
      <Setter Property="Cursor"       Value="Hand"/>
      <Setter Property="BorderThickness" Value="0"/>
      <Setter Property="Template">
        <Setter.Value>
          <ControlTemplate TargetType="Button">
            <Border Background="{TemplateBinding Background}" CornerRadius="8">
              <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Border>
            <ControlTemplate.Triggers>
              <Trigger Property="IsMouseOver" Value="True">
                <Setter Property="Background" Value="#FFB84D"/>
              </Trigger>
              <Trigger Property="IsPressed"   Value="True">
                <Setter Property="Background" Value="#D4880A"/>
              </Trigger>
            </ControlTemplate.Triggers>
          </ControlTemplate>
        </Setter.Value>
      </Setter>
    </Style>

    <!-- Secondary (Skip) button -->
    <Style x:Key="SecondaryBtn" TargetType="Button">
      <Setter Property="Background"   Value="#252525"/>
      <Setter Property="Foreground"   Value="#888888"/>
      <Setter Property="FontFamily"   Value="Segoe UI Variable Display, Segoe UI"/>
      <Setter Property="FontSize"     Value="13"/>
      <Setter Property="FontWeight"   Value="SemiBold"/>
      <Setter Property="Height"       Value="36"/>
      <Setter Property="Width"        Value="148"/>
      <Setter Property="Cursor"       Value="Hand"/>
      <Setter Property="BorderThickness" Value="0"/>
      <Setter Property="Template">
        <Setter.Value>
          <ControlTemplate TargetType="Button">
            <Border Background="{TemplateBinding Background}" CornerRadius="8">
              <ContentPresenter HorizontalAlignment="Center" VerticalAlignment="Center"/>
            </Border>
            <ControlTemplate.Triggers>
              <Trigger Property="IsMouseOver" Value="True">
                <Setter Property="Background" Value="#2E2E2E"/>
                <Setter Property="Foreground" Value="#AAAAAA"/>
              </Trigger>
              <Trigger Property="IsPressed"   Value="True">
                <Setter Property="Background" Value="#1C1C1C"/>
              </Trigger>
            </ControlTemplate.Triggers>
          </ControlTemplate>
        </Setter.Value>
      </Setter>
    </Style>

    <!-- Close (X) button -->
    <Style x:Key="CloseStyle" TargetType="Button">
      <Setter Property="Background"      Value="Transparent"/>
      <Setter Property="Foreground"      Value="#555555"/>
      <Setter Property="FontFamily"      Value="Segoe UI"/>
      <Setter Property="FontSize"        Value="11"/>
      <Setter Property="Width"           Value="26"/>
      <Setter Property="Height"          Value="26"/>
      <Setter Property="Cursor"          Value="Hand"/>
      <Setter Property="BorderThickness" Value="0"/>
      <Setter Property="Template">
        <Setter.Value>
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
        </Setter.Value>
      </Setter>
    </Style>

  </Window.Resources>

  <!-- Root card -->
  <Border Background="#181818" CornerRadius="14" Margin="10">
    <Border.Effect>
      <DropShadowEffect BlurRadius="32" ShadowDepth="8" Opacity="0.55" Color="#000000"/>
    </Border.Effect>

    <Grid>
      <Grid.RowDefinitions>
        <RowDefinition Height="48"/>   <!-- title bar -->
        <RowDefinition Height="*"/>    <!-- body -->
        <RowDefinition Height="1"/>    <!-- divider -->
        <RowDefinition Height="64"/>   <!-- buttons -->
      </Grid.RowDefinitions>

      <!-- ── Title bar ── -->
      <Grid Grid.Row="0" x:Name="DragBar">
        <StackPanel Orientation="Horizontal" VerticalAlignment="Center" Margin="18,0,0,0">
          <!-- Accent bar replacing icon -->
          <Border Width="3" Height="18" Background="#F5A623" CornerRadius="2" Margin="0,0,10,0"/>
          <StackPanel VerticalAlignment="Center">
            <TextBlock Text="LeetCode Tracker"
                       FontFamily="Segoe UI Variable Display, Segoe UI"
                       FontSize="13" FontWeight="SemiBold" Foreground="#EEEEEE"/>
            <TextBlock Text="Daily Progress Sync"
                       FontFamily="Segoe UI" FontSize="10" Foreground="#555555"/>
          </StackPanel>
        </StackPanel>
        <!-- Close -->
        <Button x:Name="CloseBtn" Style="{StaticResource CloseStyle}"
                Content="x" HorizontalAlignment="Right" Margin="0,0,12,0"
                FontWeight="SemiBold"/>
      </Grid>

      <!-- ── Stats body ── -->
      <StackPanel Grid.Row="1" Margin="18,8,18,12" VerticalAlignment="Center">

        <!-- Stat cards row -->
        <Grid>
          <Grid.ColumnDefinitions>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="8"/>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="8"/>
            <ColumnDefinition Width="*"/>
            <ColumnDefinition Width="8"/>
            <ColumnDefinition Width="*"/>
          </Grid.ColumnDefinitions>

          <!-- Total -->
          <Border Grid.Column="0" Background="#222222" CornerRadius="9" Padding="0,12">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="TOTAL" FontFamily="Segoe UI" FontSize="9" FontWeight="Bold"
                         Foreground="#505050" HorizontalAlignment="Center" Margin="0,0,0,4"/>
              <TextBlock x:Name="TotalText" FontFamily="Segoe UI Variable Display, Segoe UI"
                         FontSize="24" FontWeight="Bold" Foreground="#FFFFFF" HorizontalAlignment="Center"/>
            </StackPanel>
          </Border>

          <!-- Easy -->
          <Border Grid.Column="2" Background="#192819" CornerRadius="9" Padding="0,12">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="EASY" FontFamily="Segoe UI" FontSize="9" FontWeight="Bold"
                         Foreground="#2E5C2E" HorizontalAlignment="Center" Margin="0,0,0,4"/>
              <TextBlock x:Name="EasyText" FontFamily="Segoe UI Variable Display, Segoe UI"
                         FontSize="24" FontWeight="Bold" Foreground="#4ADE80" HorizontalAlignment="Center"/>
            </StackPanel>
          </Border>

          <!-- Medium -->
          <Border Grid.Column="4" Background="#22200F" CornerRadius="9" Padding="0,12">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="MED" FontFamily="Segoe UI" FontSize="9" FontWeight="Bold"
                         Foreground="#5C4A10" HorizontalAlignment="Center" Margin="0,0,0,4"/>
              <TextBlock x:Name="MediumText" FontFamily="Segoe UI Variable Display, Segoe UI"
                         FontSize="24" FontWeight="Bold" Foreground="#F5A623" HorizontalAlignment="Center"/>
            </StackPanel>
          </Border>

          <!-- Hard -->
          <Border Grid.Column="6" Background="#221818" CornerRadius="9" Padding="0,12">
            <StackPanel HorizontalAlignment="Center">
              <TextBlock Text="HARD" FontFamily="Segoe UI" FontSize="9" FontWeight="Bold"
                         Foreground="#5C2020" HorizontalAlignment="Center" Margin="0,0,0,4"/>
              <TextBlock x:Name="HardText" FontFamily="Segoe UI Variable Display, Segoe UI"
                         FontSize="24" FontWeight="Bold" Foreground="#F87171" HorizontalAlignment="Center"/>
            </StackPanel>
          </Border>
        </Grid>

        <!-- Last synced label -->
        <TextBlock x:Name="LastUpdatedText"
                   FontFamily="Segoe UI" FontSize="10" Foreground="#3A3A3A"
                   HorizontalAlignment="Center" Margin="0,10,0,0"/>
      </StackPanel>

      <!-- Divider -->
      <Border Grid.Row="2" Background="#242424"/>

      <!-- ── Buttons ── -->
      <StackPanel Grid.Row="3" Orientation="Horizontal"
                  HorizontalAlignment="Center" VerticalAlignment="Center" Margin="0">
        <Button x:Name="YesBtn" Style="{StaticResource PrimaryBtn}" Content="Sync Now"  Margin="0,0,10,0"/>
        <Button x:Name="NoBtn"  Style="{StaticResource SecondaryBtn}" Content="Skip"/>
      </StackPanel>

    </Grid>
  </Border>
</Window>
"@

# -- Build window ---------------------------------------------
$reader = New-Object System.Xml.XmlNodeReader $xaml
$window = [Windows.Markup.XamlReader]::Load($reader)

$window.FindName("TotalText").Text       = "$totalSolved"
$window.FindName("EasyText").Text        = "$easySolved"
$window.FindName("MediumText").Text      = "$mediumSolved"
$window.FindName("HardText").Text        = "$hardSolved"
$window.FindName("LastUpdatedText").Text = "$lastUpdated"

# Drag
$window.FindName("DragBar").Add_MouseLeftButtonDown({ $window.DragMove() })

# Button logic
$result = $false
$window.FindName("YesBtn").Add_Click({  $script:result = $true;  $window.Close() })
$window.FindName("NoBtn").Add_Click({   $script:result = $false; $window.Close() })
$window.FindName("CloseBtn").Add_Click({ $script:result = $false; $window.Close() })

$window.ShowDialog() | Out-Null

# -- Launch updater if confirmed ------------------------------
if ($result) {
    Start-Process powershell.exe `
        -ArgumentList "-WindowStyle Hidden -ExecutionPolicy Bypass -File `"C:\Users\Sanskar Phougat\Desktop\DSA\Leetcode\update_progress.ps1`"" `
        -WindowStyle Hidden

    # Minimal bottom-right toast (no emojis)
    [xml]$toastXaml = @"
<Window xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation"
        Width="300" Height="60"
        WindowStartupLocation="Manual"
        ResizeMode="NoResize" WindowStyle="None"
        AllowsTransparency="True" Background="Transparent" Topmost="True">
  <Border Background="#1E1E1E" CornerRadius="10" Margin="6">
    <Border.Effect>
      <DropShadowEffect BlurRadius="18" ShadowDepth="4" Opacity="0.5" Color="#000000"/>
    </Border.Effect>
    <Grid Margin="14,0">
      <Grid.ColumnDefinitions>
        <ColumnDefinition Width="4"/>
        <ColumnDefinition Width="12"/>
        <ColumnDefinition Width="*"/>
      </Grid.ColumnDefinitions>
      <!-- Accent stripe -->
      <Border Grid.Column="0" Background="#F5A623" CornerRadius="2" Margin="0,12,0,12"/>
      <!-- Text -->
      <StackPanel Grid.Column="2" VerticalAlignment="Center">
        <TextBlock Text="Syncing to GitHub"
                   FontFamily="Segoe UI Variable Display, Segoe UI"
                   FontSize="12" FontWeight="SemiBold" Foreground="#EEEEEE"/>
        <TextBlock Text="Progress update running in background"
                   FontFamily="Segoe UI" FontSize="10" Foreground="#555555"/>
      </StackPanel>
    </Grid>
  </Border>
</Window>
"@
    $tr = New-Object System.Xml.XmlNodeReader $toastXaml
    $toast = [Windows.Markup.XamlReader]::Load($tr)
    $screen    = [System.Windows.Forms.Screen]::PrimaryScreen.WorkingArea
    $toast.Left = $screen.Right  - 318
    $toast.Top  = $screen.Bottom - 80
    $toast.Show()
    Start-Sleep -Seconds 3
    $toast.Close()
}
