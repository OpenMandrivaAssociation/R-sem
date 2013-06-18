%global packname  sem
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.1_1
Release:          2
Summary:          Structural Equation Models
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-1.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-stats R-MASS R-matrixcalc R-boot R-tcltk R-polycor
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats R-MASS R-matrixcalc R-boot R-tcltk R-polycor

%description
This package contains functions for fitting general linear structural
equation models (with observed and unobserved variables) using the RAM
approach, and for fitting structural equations in observed-variable models
by two-stage least squares.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGES
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/etc
%{rlibdir}/%{packname}/help
