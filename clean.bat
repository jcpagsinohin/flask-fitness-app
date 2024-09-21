@echo off
setlocal

REM Database connection parameters
set PGPASSWORD=admin
set PGUSER=postgres
set PGHOST=localhost
set PGPORT=5432
set DBNAME=fitness

REM Drop the database
echo Dropping database %DBNAME%...
psql -U %PGUSER% -h %PGHOST% -p %PGPORT% -d postgres -c "DROP DATABASE IF EXISTS %DBNAME%;"

if %ERRORLEVEL% neq 0 (
    echo Failed to drop database %DBNAME%.
    exit /b %ERRORLEVEL%
)

echo Database %DBNAME% dropped successfully.

REM Create database 'fitness'
echo Creating database %DBNAME%...
psql -U %PGUSER% -h %PGHOST% -p %PGPORT% -d postgres -c "CREATE DATABASE %DBNAME%;"

if %ERRORLEVEL% neq 0 (
    echo Failed to create database %DBNAME%.
    exit /b %ERRORLEVEL%
)

echo Database %DBNAME% created successfully.

REM Remove existing migrations folder
echo Removing existing migrations folder...
rmdir /S /Q .\migrations\

REM Run Flask scripts
echo Running Flask migrations...
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

echo Seeding the database...
flask seed

if %ERRORLEVEL% neq 0 (
    echo Failed to populate database %DBNAME%.
    exit /b %ERRORLEVEL%
)

echo Successfully populated the database.

endlocal
