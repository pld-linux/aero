#
Summary:	Simulation program based on rigid body systems
Name:		aero
Version:	1.7.0
Release:	0.1
License:	Public domain
Group:		Applications
Source0:	http://robotics.ee.uwa.edu.au/aero/ftp/%{name}_%{version}_src.tar.gz
# Source0-md5:	2ea6f065bc77162ce6b4f4c4a17a3636
URL:		http://robotics.ee.uwa.edu.au/aero/ftp/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AERO is a simulation program based on rigid body systems. With the built-in 
3D editor you can create a virtual scene consisting of spheres, boxes 
(cuboids), cylinders and plains. These objects may be connected with links 
like spring, damper, rod and joint.

%prep
%setup -q -n %{name}
cp src/Makefile{.linux,}

%build

cd src 
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

%if 0
# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%endif

# initscript and its config
%if %{with initscript}
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
%endif

#%{_examplesdir}/%{name}-%{version}

%if %{with subpackage}
%files subpackage
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
%endif
