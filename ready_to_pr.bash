#!/bin/bash

# Runs unit tests, service tests, flake8, and tslint in parallel. This can be run to see verify that a branch is
# ready to be PRed. For clarity, this script suppresses all outputs of the test jobs. If a job fails, it
# displays the command to run to see the output
main() {
    BLACK="\033[0;30m"
    RED="\033[0;31m"
    GREEN="\033[0;32m"
    PIDS=""
    # Unit tests
    { nosetests --exclude-dir=app/service_tests & } &> /dev/null
    UNIT_TESTS_PID=$!
    PIDS+="$UNIT_TESTS_PID "

    # Flake8
    { flake8 . & } &> /dev/null
    FLAKE8_PID=$!
    PIDS+="$FLAKE8_PID "

    # tslint
    {  ./app/static/node_modules/tslint/bin/tslint --project app/static/tsconfig.json & } &> /dev/null
    TSLINT_PID=$!
    PIDS+="$TSLINT_PID "

    # service tests
    { nosetests app/service_tests & } &> /dev/null
    SERVICE_TESTS_PID=$!
    PIDS+="$SERVICE_TESTS_PID "

    # wait on process and see if they succeeded
    NUM_FAILURES=0
    for p in $PIDS; do
        case "$p" in
        $FLAKE8_PID )
            COMMAND_NAME="flake8"
            INSTRUCTIONS="Run flake8 . to view what went wrong"
            ;;
        $UNIT_TESTS_PID )
            COMMAND_NAME="unit tests"
            INSTRUCTIONS="Run nosetests --exclude-dir=app/service_tests to view what went wrong"
            ;;
        $SERVICE_TESTS_PID )
            COMMAND_NAME="service tests"
            INSTRUCTIONS="Run nosetests app/service_tests to view what went wrong"
            ;;
         $TSLINT_PID )
            COMMAND_NAME="tslint"
            INSTRUCTIONS="Run ./app/static/node_modules/tslint/bin/tslint --project app/static/tsconfig.json to view what went wrong"
            ;;
        esac
        wait $p
        if [ $? -eq 0 ]; then
            echo -e "$COMMAND_NAME ${GREEN}passed$BLACK."
            echo ""  # new line
        else
            echo -e "$COMMAND_NAME ${RED}FAILED$BLACK"
            echo $INSTRUCTIONS
            echo ""  # new line
            NUM_FAILURES=$((NUM_FAILURES + 1))
        fi
     done;
     if [ $NUM_FAILURES -eq 0 ]; then
        echo -e "all test types ${GREEN}passed$BLACK."
        echo -e "${GREEN}SUCCESS$BLACK"
     else
        echo -e "$NUM_FAILURES test types ${RED}failed$BLACK."
        echo -e "${RED}FAILURE$BLACK"
     fi
}

main
