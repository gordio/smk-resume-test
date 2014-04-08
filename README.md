Development environment required
=======

 * python-2.7
 * virtualenv
 * fabric


Usage
=====

0. Configure `settings_local.py` exmpl: `cp ./smk_resume/settings_local{_example,}.py`
1. `fab build` - build site environment
2. `fab run` or `fab run:0.0.0.0:8080` - run dev server4
