#!/bin/bash

export PGUSER="postgres"

psql -c "CREATE DATABASE words"

psql words -c "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\";"
