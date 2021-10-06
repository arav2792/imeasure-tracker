#!/bin/bash
set -x
cat /home/itadmin/imeasure-tracker/imeasure-mail/output.txt | mail -s "unresolved and unattended tickets" ramesh.krishna@iopex.com

