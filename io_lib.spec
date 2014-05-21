%define major	1
%define libname	%mklibname %{name} %{major}
%define develname %mklibname -d %{name}

Name:		io_lib
Version:	1.13.5
Release:	1
Summary:	General purpose trace file library

License:	GPL
Group:		Development/C
Url:		http://staden.sourceforge.net/
Source0:		http://sourceforge.net/projects/staden/files/io_lib/1.13.5/%{name}-%{version}.tar.gz
Source100: %{name}.rpmlintrc
BuildRequires:  zlib-devel

%description
Io_lib is a library of file reading and writing code to provide a general
purpose trace file (and Experiment File) reading interface. The programmer
simply calls the (eg) read_reading to create a "Read" C structure with the
data loaded into memory.

%package -n %{libname}
Summary:        Main library for %{name}

Group:          System/Libraries
Provides:       lib%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run %{name}.

%package -n %{develname}
Summary:    Development header files for %{name}

Group:      Development/C
Requires:   %{libname} = %{version}-%{release}
Provides:   %{name}-devel = %{version}-%{release}
Obsoletes:  %mklibname -d %{name} 1.9.0

%description -n %{develname}
Libraries, include files and other resources you can use to develop
%{name} applications.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall

%files
%defattr (-,root,root)
%doc CHANGES COPYRIGHT README
%{_bindir}/*

%files -n %{libname}
%defattr (-,root,root)
%{_libdir}/libstaden-read.so.*

%files -n %{develname}
%defattr (-,root,root)
%{_includedir}/%{name}
%{_libdir}/libstaden-read.a
%{_libdir}/libstaden-read.so
%{_mandir}/*/*




