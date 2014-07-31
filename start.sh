#!/usr/bin/env bash

SCREEN_NAME="stockz_server"
SCREEN_COMMAND="screen -dmS ${SCREEN_NAME}"

COMMAND="python app.py"

if ! hash screen 2> /dev/null; then
	echo "screen not found in PATH"
	exit 1
fi

if screen -list | grep -q ${SCREEN_NAME}; then
	echo "session already running"
	echo "use \"screen -r ${SCREEN_NAME}\" to reattach"
	exit 1
fi

${SCREEN_COMMAND} ${COMMAND}

echo "started \"${COMMAND}\" on \"${SCREEN_NAME}\""
echo "use \"screen -r ${SCREEN_NAME}\" to reattach"
