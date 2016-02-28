Python paste deploy
===============================

I wrote this test to know how [Paste] (http://pythonpaste.org/) and
[PasteDeploy] (http://pythonpaste.org/deploy/)work.

How to test
------------------------------------------------------
* Export `testdeploy.py` via `PYTHONPATH`

  * `export PYTHONPATH="/home/peter/paste"`

* cd to `/home/peter/paste` and run

  * `python testdeploy.py`

* Test it via `curl`

    ```
    curl -v -H "X-Auth-Token: peter"
    "http://localhost:8088/author?username=root&password=123"
    ```
    or
    ```
    curl -v -H "X-Auth-Token: peter"
    "http://localhost:8088/version?username=root&password=123"
    ```
