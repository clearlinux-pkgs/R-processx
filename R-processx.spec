#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-processx
Version  : 3.3.0
Release  : 19
URL      : https://cran.r-project.org/src/contrib/processx_3.3.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/processx_3.3.0.tar.gz
Summary  : Execute and Control System Processes
Group    : Development/Tools
License  : MIT
Requires: R-processx-lib = %{version}-%{release}
Requires: R-cli
Requires: R-withr
BuildRequires : R-assertthat
BuildRequires : R-callr
BuildRequires : R-cli
BuildRequires : R-ps
BuildRequires : R-withr
BuildRequires : buildreq-R

%description
# processx
> Execute and Control System Processes
[![lifecycle](https://img.shields.io/badge/lifecycle-maturing-blue.svg)](https://tidyverse.org/lifecycle/#maturing)
[![Linux Build Status](https://travis-ci.org/r-lib/processx.svg?branch=master)](https://travis-ci.org/r-lib/processx)
[![Windows Build status](https://ci.appveyor.com/api/projects/status/15sfg3l9mm4aseyf/branch/master?svg=true)](https://ci.appveyor.com/project/gaborcsardi/processx)
[![](https://www.r-pkg.org/badges/version/processx)](https://www.r-pkg.org/pkg/processx)
[![CRAN RStudio mirror downloads](https://cranlogs.r-pkg.org/badges/processx)](https://www.r-pkg.org/pkg/processx)
[![Coverage Status](https://img.shields.io/codecov/c/github/r-lib/processx/master.svg)](https://codecov.io/github/r-lib/processx?branch=master)

%package lib
Summary: lib components for the R-processx package.
Group: Libraries

%description lib
lib components for the R-processx package.


%prep
%setup -q -c -n processx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552842615

%install
export SOURCE_DATE_EPOCH=1552842615
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library processx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library processx
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library processx
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  processx || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/processx/CODE_OF_CONDUCT.md
/usr/lib64/R/library/processx/DESCRIPTION
/usr/lib64/R/library/processx/INDEX
/usr/lib64/R/library/processx/LICENSE
/usr/lib64/R/library/processx/Meta/Rd.rds
/usr/lib64/R/library/processx/Meta/features.rds
/usr/lib64/R/library/processx/Meta/hsearch.rds
/usr/lib64/R/library/processx/Meta/links.rds
/usr/lib64/R/library/processx/Meta/nsInfo.rds
/usr/lib64/R/library/processx/Meta/package.rds
/usr/lib64/R/library/processx/NAMESPACE
/usr/lib64/R/library/processx/NEWS.md
/usr/lib64/R/library/processx/R/processx
/usr/lib64/R/library/processx/R/processx.rdb
/usr/lib64/R/library/processx/R/processx.rdx
/usr/lib64/R/library/processx/bin/px
/usr/lib64/R/library/processx/bin/supervisor
/usr/lib64/R/library/processx/help/AnIndex
/usr/lib64/R/library/processx/help/aliases.rds
/usr/lib64/R/library/processx/help/paths.rds
/usr/lib64/R/library/processx/help/processx.rdb
/usr/lib64/R/library/processx/help/processx.rdx
/usr/lib64/R/library/processx/html/00Index.html
/usr/lib64/R/library/processx/html/R.css
/usr/lib64/R/library/processx/tests/testthat.R
/usr/lib64/R/library/processx/tests/testthat/fixtures/simple.txt
/usr/lib64/R/library/processx/tests/testthat/helper.R
/usr/lib64/R/library/processx/tests/testthat/test-assertions.R
/usr/lib64/R/library/processx/tests/testthat/test-chr-io.R
/usr/lib64/R/library/processx/tests/testthat/test-cleanup.R
/usr/lib64/R/library/processx/tests/testthat/test-connections.R
/usr/lib64/R/library/processx/tests/testthat/test-env.R
/usr/lib64/R/library/processx/tests/testthat/test-extra-connections.R
/usr/lib64/R/library/processx/tests/testthat/test-io.R
/usr/lib64/R/library/processx/tests/testthat/test-kill-tree.R
/usr/lib64/R/library/processx/tests/testthat/test-poll-connections.R
/usr/lib64/R/library/processx/tests/testthat/test-poll-stress.R
/usr/lib64/R/library/processx/tests/testthat/test-poll.R
/usr/lib64/R/library/processx/tests/testthat/test-poll2.R
/usr/lib64/R/library/processx/tests/testthat/test-poll3.R
/usr/lib64/R/library/processx/tests/testthat/test-print.R
/usr/lib64/R/library/processx/tests/testthat/test-process.R
/usr/lib64/R/library/processx/tests/testthat/test-ps-methods.R
/usr/lib64/R/library/processx/tests/testthat/test-run.R
/usr/lib64/R/library/processx/tests/testthat/test-set-std.R
/usr/lib64/R/library/processx/tests/testthat/test-sigchld.R
/usr/lib64/R/library/processx/tests/testthat/test-stdin.R
/usr/lib64/R/library/processx/tests/testthat/test-stress.R
/usr/lib64/R/library/processx/tests/testthat/test-utils.R
/usr/lib64/R/library/processx/tests/testthat/test-wait.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/processx/libs/processx.so
/usr/lib64/R/library/processx/libs/processx.so.avx2
