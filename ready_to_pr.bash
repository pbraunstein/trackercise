#!/bin/bash

main() {
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
    {  ./app/static/node_modules/tslint/bin/tslint --project app/static/tsconfig.json &} &> /dev/null
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
            INSTRUCTIONS="Run cd app/static && ./node_modules/tslint/bin/tslint to view what went wrong"
            ;;
        esac
        wait $p
        if [ $? -eq 0 ]; then
            echo "$COMMAND_NAME passed."
        else
            echo "$COMMAND_NAME FAILED"
            NUM_FAILURES+=1
        fi
     done;
     if [ $NUM_FAILURES -eq 0 ]; then
        echo "SUCCESS"
     else
        echo "FAILURE"
     fi
}

main