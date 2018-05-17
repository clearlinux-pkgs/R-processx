#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-processx
Version  : 3.1.0
Release  : 8
URL      : https://cran.r-project.org/src/contrib/processx_3.1.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/processx_3.1.0.tar.gz
Summary  : Execute and Control System Processes
Group    : Development/Tools
License  : MIT
Requires: R-processx-lib
BuildRequires : clr-R-helpers

%description
It can check if a background process is running; wait on a background
    process to finish; get the exit status of finished processes; kill
    background processes and their children; restart processes. It can read
    the standard output and error of the processes, using non-blocking
    connections. 'processx' can poll a process for standard output or
    error, with a timeout. It can also poll several processes at once.

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
export SOURCE_DATE_EPOCH=1526529722

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1526529722
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
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
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library processx|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
/usr/lib64/R/library/processx/README.markdown
/usr/lib64/R/library/processx/bin/px
/usr/lib64/R/library/processx/bin/supervisor
/usr/lib64/R/library/processx/help/AnIndex
/usr/lib64/R/library/processx/help/aliases.rds
/usr/lib64/R/library/processx/help/paths.rds
/usr/lib64/R/library/processx/help/processx.rdb
/usr/lib64/R/library/processx/help/processx.rdx
/usr/lib64/R/library/processx/html/00Index.html
/usr/lib64/R/library/processx/html/R.css
/usr/lib64/R/library/processx/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/processx/libs/processx.so
/usr/lib64/R/library/processx/libs/processx.so.avx2
/usr/lib64/R/library/processx/libs/processx.so.avx512
