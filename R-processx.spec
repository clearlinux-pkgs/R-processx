#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-processx
Version  : 3.8.0
Release  : 65
URL      : https://cran.r-project.org/src/contrib/processx_3.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/processx_3.8.0.tar.gz
Summary  : Execute and Control System Processes
Group    : Development/Tools
License  : MIT
Requires: R-processx-lib = %{version}-%{release}
Requires: R-R6
Requires: R-ps
BuildRequires : R-R6
BuildRequires : R-curl
BuildRequires : R-ps
BuildRequires : buildreq-R

%description
check if a background process is running; wait on a background process
    to finish; get the exit status of finished processes; kill background
    processes. It can read the standard output and error of the processes,
    using non-blocking connections. 'processx' can poll a process for
    standard output or error, with a timeout. It can also poll several
    processes at once.

%package lib
Summary: lib components for the R-processx package.
Group: Libraries

%description lib
lib components for the R-processx package.


%prep
%setup -q -n processx
cd %{_builddir}/processx

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666842385

%install
export SOURCE_DATE_EPOCH=1666842385
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/processx/bin/sock
/usr/lib64/R/library/processx/bin/supervisor
/usr/lib64/R/library/processx/help/AnIndex
/usr/lib64/R/library/processx/help/aliases.rds
/usr/lib64/R/library/processx/help/figures/lifecycle-archived.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-defunct.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-deprecated.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-experimental.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-maturing.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-questioning.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-stable.svg
/usr/lib64/R/library/processx/help/figures/lifecycle-superseded.svg
/usr/lib64/R/library/processx/help/paths.rds
/usr/lib64/R/library/processx/help/processx.rdb
/usr/lib64/R/library/processx/help/processx.rdx
/usr/lib64/R/library/processx/html/00Index.html
/usr/lib64/R/library/processx/html/R.css
/usr/lib64/R/library/processx/include/processx/unix-sockets.c
/usr/lib64/R/library/processx/include/processx/unix-sockets.h
/usr/lib64/R/library/processx/tests/testthat.R
/usr/lib64/R/library/processx/tests/testthat/_snaps/err-output.md
/usr/lib64/R/library/processx/tests/testthat/_snaps/errors.md
/usr/lib64/R/library/processx/tests/testthat/fixtures/simple.txt
/usr/lib64/R/library/processx/tests/testthat/helper.R
/usr/lib64/R/library/processx/tests/testthat/test-assertions.R
/usr/lib64/R/library/processx/tests/testthat/test-chr-io.R
/usr/lib64/R/library/processx/tests/testthat/test-cleanup.R
/usr/lib64/R/library/processx/tests/testthat/test-client-lib.R
/usr/lib64/R/library/processx/tests/testthat/test-connections.R
/usr/lib64/R/library/processx/tests/testthat/test-env.R
/usr/lib64/R/library/processx/tests/testthat/test-err-output.R
/usr/lib64/R/library/processx/tests/testthat/test-err.R
/usr/lib64/R/library/processx/tests/testthat/test-errors.R
/usr/lib64/R/library/processx/tests/testthat/test-extra-connections.R
/usr/lib64/R/library/processx/tests/testthat/test-fifo.R
/usr/lib64/R/library/processx/tests/testthat/test-io.R
/usr/lib64/R/library/processx/tests/testthat/test-kill-tree.R
/usr/lib64/R/library/processx/tests/testthat/test-poll-connections.R
/usr/lib64/R/library/processx/tests/testthat/test-poll-curl.R
/usr/lib64/R/library/processx/tests/testthat/test-poll-stress.R
/usr/lib64/R/library/processx/tests/testthat/test-poll.R
/usr/lib64/R/library/processx/tests/testthat/test-poll2.R
/usr/lib64/R/library/processx/tests/testthat/test-poll3.R
/usr/lib64/R/library/processx/tests/testthat/test-print.R
/usr/lib64/R/library/processx/tests/testthat/test-process.R
/usr/lib64/R/library/processx/tests/testthat/test-ps-methods.R
/usr/lib64/R/library/processx/tests/testthat/test-pty.R
/usr/lib64/R/library/processx/tests/testthat/test-run.R
/usr/lib64/R/library/processx/tests/testthat/test-set-std.R
/usr/lib64/R/library/processx/tests/testthat/test-sigchld.R
/usr/lib64/R/library/processx/tests/testthat/test-stdin.R
/usr/lib64/R/library/processx/tests/testthat/test-stress.R
/usr/lib64/R/library/processx/tests/testthat/test-unix-sockets.R
/usr/lib64/R/library/processx/tests/testthat/test-utf8.R
/usr/lib64/R/library/processx/tests/testthat/test-utils.R
/usr/lib64/R/library/processx/tests/testthat/test-wait.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/processx/libs/client.so
/usr/lib64/R/library/processx/libs/client.so.avx2
/usr/lib64/R/library/processx/libs/client.so.avx512
/usr/lib64/R/library/processx/libs/processx.so
/usr/lib64/R/library/processx/libs/processx.so.avx2
/usr/lib64/R/library/processx/libs/processx.so.avx512
