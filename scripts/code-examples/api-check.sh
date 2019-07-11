#!/usr/bin/env bash
set -exuo pipefail

STATUS_CODE=`curl -s -m 10 -o /dev/null -w "%{http_code}\n" ${SCHEME}://${HOST}`
EXPECTED_CODE=200

if [ $STATUS_CODE -eq $EXPECTED_CODE ]; then
  echo "API response check passed ($STATUS_CODE})";
else
  echo "API response check failed (${SCHEME}://${HOST})";
  echo "expected: " $EXPECTED_CODE;
  echo "actual: " $STATUS_CODE;
  travis_terminate 1;
fi
