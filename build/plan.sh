pkg_origin=gregorio
pkg_name=teste
pkg_version=0.1.0
pkg_maintainer="App Flask"
pkg_description="Test app flask"
pkg_license=("MIT")
pkg_source="fake"
pkg_svc_user=root
pkg_svc_group=root
pkg_build_deps=(
		core/virtualenv
		python/python

)

pkg_deps=(
		core/python2
		core/mongo-tools
		#core/coreutils
		#smartb/python
		#core/mongodb
		#core/python2
		#python/python
		#core/python
		#core/python2
)

pkg_binds=(
		[database] = mongod.net.port
)

pkg_exports=(
		[port]=server.port
)

pkg_exposes=(port)


pkg_lib_dirs=(lib)
pkg_bin_dirs=(bin)
pkg_include_dirs=(include)
pkg_interpreters=(bin/python bin/python3 bin/python3.5)
#pkg_svc_run="mongod --config $pkg_svc_config_path/mongod.conf"


do_download(){
	return 0
}


do_verify(){
	return 0
}


do_clean(){
	return 0
}


do_unpack(){
	PROJECT_ROOT="${PLAN_CONTEXT}/.."

	mkdir -p $pkg_prefix
	build_line "Copying project data to $pkg_prefix"
	cp -r $PROJECT_ROOT/app $pkg_prefix/
  cp -r $PROJECT_ROOT/*.py $pkg_prefix/
  cp -r $PROJECT_ROOT/requirements.txt $pkg_prefix/


}


do_build(){
	return 0
}



do_install(){
	cd $pkg_prefix
  virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
}
