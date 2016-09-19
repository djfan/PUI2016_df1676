#PUI2016_df1676
<br/>HW2_df1676
<br/>
<br/>Dongjie Fan
<br/>NetID: df1676
<br/>Github: Alan-F
<br/>
<br/>Group: Dongjie Fan, Ziman Zhou and Kai Qu 
<br/>
<br/>##**Assignment 1: tracking each vehicle for a line**
<br/>Name: show_bus_locations_df1676.py
<br/>https://github.com/Alan-F/PUI2016_df1676/blob/master/HW2_df1676/show_bus_locations_df1676.py
<br/>
<br/>Users can input "python show_bus_locations_df1676.py <MTA_KEY> <BUS_LINE>" in command line 
and will get information about current locations of all active buses from the specific bus line.
<br/>User can find all New York bus line numbers in MTA's website and make sure not to input invalid bus number.
<br/>The bus line name is case-sensitive.
<br/>
<br/>##**Assignment 2: next stop information**
<br/>Name: get_bus_info_df1676.py
<br/>https://github.com/Alan-F/PUI2016_df1676/blob/master/HW2_df1676/get_bus_info_df1676.py
<br/>Users can input "python get_bus_info_df1676.py <MTA_KEY> <BUS_LINE> <BUS_LINE>.csv" in command line 
and will get information on the next stop location of all busses of a given line
<br/>When the OnwardCalls field is empty, output will be “N/A” as values for both the “Stop Name” and “Stop Status” fields.
<br/>
<br/>##**Assignment 3: Read CSV files with pandas**
<br/>https://github.com/Alan-F/PUI2016_df1676/blob/master/HW2_df1676/HW2_3_df1676.ipynb
<br/>Dataset Location is "/gws/open/NYCOpenData/nycopendata/data//zkky-n5j3/1414246141/zkky-n5j3
<br/>Firstly, create the env variable "DFDATA" to point to "/gws/open/NYCOpenData/nycopendata/data"
<br/>Secondly, load data and show the top 5 rows of the data.
<br/>Thirdly, keep two columns "Neversink Elevation" and "Rondout Elevation" which contain numeric data, and drop other columns.
Show the top several rows of this new data frame.
<br/>Then draw scatter plot "Elevation: Neversink V.S. Rondout" by using DataFrame.plot function.
<br/>Besides, draw the same plot by using pylab.scatter function. 
<br/>
<br/>##**Extra Credit Assignment : work with dates in Pandas**
<br/>https://github.com/Alan-F/PUI2016_df1676/blob/master/HW2_df1676/HW2_ExtraCredit_df1676.ipynb
<br/>Use the same dataset as Assignment 3.
<br/>Select two columns "Neversink Date"(date/time column) and "Neversink Elevation"(numeric column) and make a plot.
<br>The plot shows that the elevation of Neversink has changed with time (from Mar 2005 to Sep  2010).
