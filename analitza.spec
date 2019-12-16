#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : analitza
Version  : 19.12.0
Release  : 20
URL      : https://download.kde.org/stable/release-service/19.12.0/src/analitza-19.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.0/src/analitza-19.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.0/src/analitza-19.12.0.tar.xz.sig
Summary  : A library to add mathematical features to your program
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0
Requires: analitza-data = %{version}-%{release}
Requires: analitza-lib = %{version}-%{release}
Requires: analitza-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : eigen-dev
BuildRequires : glew-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the analitza package.
Group: Data

%description data
data components for the analitza package.


%package dev
Summary: dev components for the analitza package.
Group: Development
Requires: analitza-lib = %{version}-%{release}
Requires: analitza-data = %{version}-%{release}
Provides: analitza-devel = %{version}-%{release}
Requires: analitza = %{version}-%{release}
Requires: analitza = %{version}-%{release}

%description dev
dev components for the analitza package.


%package lib
Summary: lib components for the analitza package.
Group: Libraries
Requires: analitza-data = %{version}-%{release}
Requires: analitza-license = %{version}-%{release}

%description lib
lib components for the analitza package.


%package license
Summary: license components for the analitza package.
Group: Default

%description license
license components for the analitza package.


%prep
%setup -q -n analitza-19.12.0
cd %{_builddir}/analitza-19.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576540549
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576540549
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/analitza
cp %{_builddir}/analitza-19.12.0/COPYING %{buildroot}/usr/share/package-licenses/analitza/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/analitza-19.12.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/analitza/1bd373e4851a93027ba70064bd7dbdc6827147e1
cp %{_builddir}/analitza-19.12.0/COPYING.LIB %{buildroot}/usr/share/package-licenses/analitza/ba8966e2473a9969bdcab3dc82274c817cfd98a1
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/libanalitza/plots/3Ds.plots
/usr/share/libanalitza/plots/basic_curves.plots
/usr/share/libanalitza/plots/conics.plots
/usr/share/libanalitza/plots/polar.plots
/usr/share/locale/ar/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/bs/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ca/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/cs/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/da/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/de/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/el/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/es/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/et/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/fi/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/fr/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ga/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/gl/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/hu/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/it/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ja/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/kk/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/lt/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/lv/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ml/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/mr/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/nb/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/nds/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/nl/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/nn/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/pl/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/pt/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ru/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/sk/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/sl/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/sv/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/tr/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/ug/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/uk/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/analitza_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/analitza_qt.qm

%files dev
%defattr(-,root,root,-)
/usr/include/Analitza5/analitza/abstractexpressionvisitor.h
/usr/include/Analitza5/analitza/abstractlexer.h
/usr/include/Analitza5/analitza/analitzaexport.h
/usr/include/Analitza5/analitza/analitzautils.h
/usr/include/Analitza5/analitza/analyzer.h
/usr/include/Analitza5/analitza/apply.h
/usr/include/Analitza5/analitza/builtinmethods.h
/usr/include/Analitza5/analitza/container.h
/usr/include/Analitza5/analitza/customobject.h
/usr/include/Analitza5/analitza/expression.h
/usr/include/Analitza5/analitza/expressionstream.h
/usr/include/Analitza5/analitza/expressiontype.h
/usr/include/Analitza5/analitza/importqobjectmetatype.h
/usr/include/Analitza5/analitza/list.h
/usr/include/Analitza5/analitza/matrix.h
/usr/include/Analitza5/analitza/object.h
/usr/include/Analitza5/analitza/operations.h
/usr/include/Analitza5/analitza/operator.h
/usr/include/Analitza5/analitza/value.h
/usr/include/Analitza5/analitza/variable.h
/usr/include/Analitza5/analitza/variables.h
/usr/include/Analitza5/analitza/vector.h
/usr/include/Analitza5/analitza_version.h
/usr/include/Analitza5/analitzagui/algebrahighlighter.h
/usr/include/Analitza5/analitzagui/analitzaguiexport.h
/usr/include/Analitza5/analitzagui/analitzawidgets_export.h
/usr/include/Analitza5/analitzagui/expressionedit.h
/usr/include/Analitza5/analitzagui/operatorsmodel.h
/usr/include/Analitza5/analitzagui/plotsview2d.h
/usr/include/Analitza5/analitzagui/plotsview3d_es.h
/usr/include/Analitza5/analitzagui/variablesmodel.h
/usr/include/Analitza5/analitzaplot/analitzaplotexport.h
/usr/include/Analitza5/analitzaplot/functiongraph.h
/usr/include/Analitza5/analitzaplot/planecurve.h
/usr/include/Analitza5/analitzaplot/plotitem.h
/usr/include/Analitza5/analitzaplot/plotsdictionarymodel.h
/usr/include/Analitza5/analitzaplot/plotsfactory.h
/usr/include/Analitza5/analitzaplot/plotsmodel.h
/usr/include/Analitza5/analitzaplot/plotter2d.h
/usr/include/Analitza5/analitzaplot/plotter3d_es.h
/usr/include/Analitza5/analitzaplot/plottingenums.h
/usr/include/Analitza5/analitzaplot/spacecurve.h
/usr/include/Analitza5/analitzaplot/surface.h
/usr/lib64/cmake/Analitza5/Analitza5Config.cmake
/usr/lib64/cmake/Analitza5/Analitza5ConfigVersion.cmake
/usr/lib64/cmake/Analitza5/Analitza5Targets-relwithdebinfo.cmake
/usr/lib64/cmake/Analitza5/Analitza5Targets.cmake
/usr/lib64/libAnalitza.so
/usr/lib64/libAnalitzaGui.so
/usr/lib64/libAnalitzaPlot.so
/usr/lib64/libAnalitzaWidgets.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libAnalitza.so.8
/usr/lib64/libAnalitza.so.8.0.0
/usr/lib64/libAnalitzaGui.so.8
/usr/lib64/libAnalitzaGui.so.8.0.0
/usr/lib64/libAnalitzaPlot.so.8
/usr/lib64/libAnalitzaPlot.so.8.0.0
/usr/lib64/libAnalitzaWidgets.so.8
/usr/lib64/libAnalitzaWidgets.so.8.0.0
/usr/lib64/qt5/qml/org/kde/analitza/Graph2D.qml
/usr/lib64/qt5/qml/org/kde/analitza/Graph3D.qml
/usr/lib64/qt5/qml/org/kde/analitza/libanalitzadeclarativeplugin.so
/usr/lib64/qt5/qml/org/kde/analitza/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/analitza/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/analitza/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/analitza/ba8966e2473a9969bdcab3dc82274c817cfd98a1
