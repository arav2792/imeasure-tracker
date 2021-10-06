<?php
$servername = "localhost";
$username = "root";
$password = "noc@nextroll";
$dbname = "Adroll";
$date = date('Y-m-d');;
$weekendDay = false;
$day = date("D", strtotime($date));
if($day == 'Sat' || $day == 'Sun'){
    $weekendDay = 'Weekend';
}
else { $weekendDay = 'Weekday'; }
$conn = new mysqli($servername, $username, $password, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$sql = "INSERT INTO `posts_post` (`id`, `weekno`, `dete`, `stime`, `rtime`, `wtime`, `itype`, `descrp`, `env`, `hostype`, `hostname`, `mode`, `engineer`, `remediation`, `escalated`, `escreason`, `status`,`escalatedto`, `resolvedteam`, `resolvedby`, `resolution`, `source`, `others`, `respteam`, `falsealarm`, `yeer`, `dayofweek`, `menth`, `shyft`,`alertname`, `ghcname`, `taskname`, `comments`,`priority`) VALUES(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+00:00'))), date(convert_tz(now(), '+00:00', '+00:00')), '01:00', '01:00', '01:00', 'GHC', 'BI Pipeline Monitoring', 'Production', 'Jenkins', 'Jenkins BI', 'Email', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'Jenkins', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+00:00')),'USA','NA','Pipeline Monitoring','NA','No issues observed','P1'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+00:00'))), date(convert_tz(now(), '+00:00', '+00:00')), '01:00', '01:00', '01:00', 'Task', 'Checked for EMR failures', 'Production', 'AWS EMR', 'aws.amazon.com', 'Manual', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+00:00')),'USA','NA','NA','EMR Job Check','No issues observed','P1'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+00:00'))), date(convert_tz(now(), '+00:00', '+00:00')), '01:00', '01:00', '01:00', 'Task', 'Checked for EMRs running for more than 12 hours', 'Production', 'AWS EMR', 'aws.amazon.com', 'Manual', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+00:00')),'USA','NA','NA','Long Running EMR Check','No issues observed','P2'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+00:00'))), date(convert_tz(now(), '+00:00', '+00:00')), '01:00', '01:00', '01:00', 'GHC', 'Monitored the Storm Topologies', 'Production', 'Storm Cluster', 'app.datadoghq.com', 'Manual', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'Datadog', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+00:00')),'USA','NA','Storm Monitoring','NA','No issues observed','P2'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+00:00'))), date(convert_tz(now(), '+00:00', '+00:00')), '01:00', '01:00', '01:00', 'GHC', 'Checked the Celery dashboard for failures', 'Production', 'Celery Worker', 'app.adroll.com/backstage/celerytasks/hud', 'Manual', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+00:00')),'USA','NA','Celery Dashboard check','NA','No issues observed','P2'),(NULL, concat('Week ', week(convert_tz(now(), '+00:00', '+00:00'))), date(convert_tz(now(), '+00:00', '+00:00')), '01:00', '01:00', '01:00', 'GHC', 'Checked the app.adroll.com dashboard', 'Production', 'Other', 'app.adroll.com', 'Manual', 'noc', 'NA', 'No', 'NA', 'Resolved','NA', 'NOC', 'noc', 'NA', 'NA', 'NA', 'NOC', 'No', year(now()), '$weekendDay', monthname(convert_tz(now(), '+00:00', '+00:00')),'USA','NA','Dashboard monitoring','NA','No issues observed','P1')";

if ($conn->query($sql) === TRUE) {
    echo $date . " USA Tickets created successfully\n";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
