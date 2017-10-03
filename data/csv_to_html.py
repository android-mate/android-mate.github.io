import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date

def get_flaw_type(flaw):
	if (flaw=="ACCESSIBILITY_SIZE_FLAW"):
		return "SIZE","Minimum touch target size is 48dp x 48dp. "
	if (flaw=="MISSING_SPEAKABLE_TEXT_FLAW"):
		return "MISSING LABEL","View is missing label for a screen reader"
	if (flaw=="ACCESSIBILITY_CONTRAST_FLAW"):
		return "CONTRAST","Contrast ratio should be at least 4.5"
	if (flaw=="EDITABLE_CONTENT_DESC_FLAW"):
		return "Content description in editable view","Editable view should have hint or label by instead of content description"
	if (flaw=="DUPLICATE_SPEAKABLE_TEXT_FLAW"):
		return "DUPLICATE LABEL","View has the same label as another view"
	if (flaw=="DUPLICATE_CLICKABLE_BOUNDS_FLAW"):
		return "Duplicate clickable bounds","View has same bounds as another view (likely a descendent)"
	if (flaw=="CLICKABLE_SPAN"):
		return "Clickable span","Clickable span should be declared as URLSpan"
	
	

	

def result_to_html(result_file, package_name):
	#os.chdir(result_dir)
	#os.system("mkdir html")
	#os.chdir(result_dir+"/html")
	postFilename = POSTS_DIR + DATE_STR + "-" + package_name + ".md"
	reportFilename = HTML_DIR + package_name

	# Get app name
	appList = FDROID.findall("application[@id='"+package_name+"']")
	if not appList:
		print "ERROR: Could not find " + package_name
		return -1
	app = appList[0]
	appName = app.find('name').text

	# Compose report
	html = "---\n"
	html += "layout: default\n"
	html += "title: MATE Report for " + appName + "\n"
	html += "---\n"
	html += "\n### Flaws in " + appName + " (" + package_name + ")\n\n"

	activities = []
	nflaws = 0
	file = open(CSV_DIR + result_file, "r")
	for line in file: 
		if (nflaws>0): #exclude header
			data = line.split(",")
			activity_name = data[1]
			activities.append(activity_name)
		nflaws += 1
    
#0 package	1 activity	2 widget_id	3 widget_type	4 widget_text	5 flaw_type	6 extra_info
	
	activities = set(activities)
	#print "amount of activities: " + str(len(activities))
	for activity in activities:
		#print activity
		#html=html+("<href="+package_name+"_"+activity+".html>"+activity+"</a>\n")
    
		#html="<html>\n"
		#html=html+("<body>\n")
		html += "\n#### Activity " + activity + "\n\n"
		html += "<table border='1'>\n"
		html += "\t<tr>\n"
		html += "\t\t<th> widget id </th>\n"
		html += "\t\t<th> widget type </th>\n"
		html += "\t\t<th> widget text </th>\n"
		html += "\t\t<th> flaw type </th>\n"
		html += "\t\t<th> info </th>\n"
		html += "\t\t<th> hint </th>\n"
		html += "\t</tr>\n"

		file = open(CSV_DIR + result_file, "r") 
		for line in file: 			
			data = line.split(",")	
			#print "   " + data[1]								
			if (activity == data[1] and len(data)>=6): #activity
				html += "\t<tr>\n"
				widget_id = data[2]
				if (widget_id != ""):
					widget_id = widget_id.replace(":","")
					html += "\t\t<td> "+widget_id+" </td>\n"
					html += "\t\t<td> "+data[3]+" </td>\n"
					html += "\t\t<td> "+data[4]+" </td>\n"
					flaw_type, tip = get_flaw_type(data[5])
					html += "\t\t<td> "+flaw_type+" </td>\n"
					if (data[5].find("SIZE")>0):
						html += "\t\t<td> "+data[6]+","+data[7].strip()+" </td>\n"
					else:
						html += "\t\t<td> "+data[6].strip()+" </td>\n"
					html += "\t\t<td> "+tip+" </td>\n"
				html += "\t</tr>\n"
		html += "</table>\n\n"

	htmlFile = open(reportFilename + ".md","a")
	htmlFile.write(html)
	htmlFile.close()

	# Compose post
	postStr = "---\n"
	postStr += "layout: post\n"
	postStr += "title: " + appName + "\n"
	postStr += "summary: " + app.find('summary').text + "\n"
	postStr += "icon: " + ICONS + app.find('icon').text + "\n"
	postStr += "nflaws: " + str(nflaws) + "\n"
	postStr += "report: " + reportFilename + ".html" + "\n"
	postStr += "---\n"

	postFile = open(postFilename,"w")
	postFile.write(postStr)
	postFile.close()

CSV_DIR = sys.argv[1]
HTML_DIR = sys.argv[2]
POSTS_DIR = sys.argv[3]
ICONS = "https://f-droid.org/repo/icons/"
FDROID_XML = 'index.xml'
FDROID = ET.parse(FDROID_XML).getroot()
DATE_STR = date.today().strftime('%Y-%m-%d')

for file in os.listdir(CSV_DIR):
	index = file.find("_")
	package_name = file[0:index]
	print package_name
	result_to_html(file, package_name)
