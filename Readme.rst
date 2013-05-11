====
Interview
====
Here are some of the most painful questions from a recent onsite interview with XXXX.
No computer was given, I was expected to whiteboard all of this. Not all the questions are provided here but the most painful ones are.


Put output from a lot of files into one file
++++++++++++++++++++++++++++++++++++++++++++

Answer Given:

::

  touch newfile
  for f in *; do
    cat $f >> newfile
  done

Answer wanted:
??


Put only ip addresses from a lot of files in current directory into one file
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

(Attempted) Answer Given:

::

  touch newfile
  sed -r -e '/([0-9]{1,3}\.){3}[0-9]{1,3}/w newfile' *.txt

extract last IP address from this output:
++++++++++++++++++++++++++++++++++++++++++

::

  +--------------------------------------+-------------+--------+-----------------------------------------+
  | ID                                   | Name        | Status | Networks                                |
  +--------------------------------------+-------------+--------+-----------------------------------------+
  | 970e4ca0-f9b7-4c44-80ed-bf0152c96ae1 | resize-demo | RESIZE | private=172.16.101.6, public=10.4.113.6 |
  +--------------------------------------+-------------+--------+-----------------------------------------+

(Attempted) Answer given:

``nova list | sed -n -r -e 's/([0-9]{1,3}\.){3}[0-9]{1,3}/&/p' | sed -n -r -e 's/.*public=(.*) \|/\1/p'``

Note: Interviewer started talking about grep

(Attempted) Answer given:

``nova list | grep -e '/([0-9]{1,3}\.){3}[0-9]{1,3}/' | sed -n -r -e 's/.*public=(.*) \|/\1/p'``

Note: Interviewer started talking about awk (I had mentioned this previously but for w/e reason didn't think it was what he was looking for)

Answer Wanted:

``nova list | grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}' | awk '{ print $9 }'``


How do you test if SSHD is running on port 22 on thousands of remote hosts?
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Answer Given:

``nmap -p22 host``

Wanted Answer:

``nc -zv host 22``

You have no way to access the host on which a guest VM is running, how do you access the guest VM
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Answer Given:

::

  virsh console
  virtconsole

Answer Wanted:
something something libvirt

.... continued
