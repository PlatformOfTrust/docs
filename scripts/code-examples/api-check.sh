#!/usr/bin/env bash
set -u

# Use an endpoint that does not require authentication
URL="${SCHEME}://${HOST}/products/v1"
echo "Executing API response check: $URL"

# Use an endpoint that does not require
STATUS_CODE=`curl -s -m 10 -o /dev/null -w "%{http_code}\n" ${SCHEME}://${HOST}/products/v1`
EXPECTED_CODE=200

if [ $STATUS_CODE -eq $EXPECTED_CODE ]; then
  echo "API response check passed ($STATUS_CODE})";
else
  echo "API response check failed.";
  echo "expected: " $EXPECTED_CODE;
  echo "actual: " $STATUS_CODE;
  exit 1;
fi
