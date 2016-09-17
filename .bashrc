#.bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# User specific aliases and functions

#compute
export DFDATA='/gws/open/NYCOpenData/nycopendata/data'
export PUI2016='/home/cusp/df1676/PUI2016_df1676/'
alias pui2016='cd $PUI2016'

#local
alias compute='ssh -X -A -t df1676@gw.cusp.nyu.edu ssh -A -X compute'
alias windows='ssh df1676@gw.cusp.nyu.edu -L 9000:wingrdp.cusp.nyu.edu:3389'
alias jupyterhub='ssh df1676@gw.cusp.nyu.edu -L 8000:compute.cusp.nyu.edu:8000'
