#!/bin/bash

echo -e "Content-type: text/html\n\n"

echo "<h1> Status of Pi: $(sp1a)</h1>"

echo "<pre>$(./pisalive)</pre>"
