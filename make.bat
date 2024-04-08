@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "check" goto check

if "%1" == "" goto help
if "%1" == "help" (
	:help
	echo.Please use `make ^<target^>` where ^<target^> is one of
	echo.  html       to make standalone HTML files
	echo.  htmlview   to open the index page built by the html target in your browser
	echo.  dirhtml    to make HTML files named index.html in directories
	echo.  singlehtml to make a single large HTML file
	echo.  pickle     to make pickle files
	echo.  json       to make JSON files
	echo.  htmlhelp   to make HTML files and a HTML help project
	echo.  qthelp     to make HTML files and a qthelp project
	echo.  devhelp    to make HTML files and a Devhelp project
	echo.  epub       to make an epub
	echo.  latex      to make LaTeX files, you can set PAPER=a4 or PAPER=letter
	echo.  text       to make text files
	echo.  man        to make manual pages
	echo.  changes    to make an overview over all changed/added/deprecated items
	echo.  linkcheck  to check all external links for integrity
	echo.  doctest    to run all doctests embedded in the documentation if enabled
	echo.  check      to check for stylistic and formal issues using sphinx-lint
	goto end
)

if "%1" == "clean" (
	for /d %%i in (%BUILDDIR%\*) do rmdir /q /s %%i
	del /q /s %BUILDDIR%\*
	goto end
)

rem Targets other than "clean", "check", "help", or "" need the
rem Sphinx build command, which the user may define via SPHINXBUILD.

if not defined SPHINXBUILD (
	rem If it is not defined, we build in a virtual environment
	if not exist venv (
		echo.    Setting up the virtual environment
		%PYTHON% -m venv venv
		echo.    Installing requirements
		venv\Scripts\python -m pip install -r requirements.txt
	)
	set PYTHON=venv\Scripts\python
	set SPHINXBUILD=venv\Scripts\sphinx-build
)


%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd

:end
popd
endlocal