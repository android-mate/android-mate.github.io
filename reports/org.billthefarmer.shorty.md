---
layout: default
title: MATE Report for Shorty
---

### Flaws in Shorty (org.billthefarmer.shorty)


#### Activity MainActivity

<table border='1'>
	<tr>
		<th> widget id </th>
		<th> widget type </th>
		<th> widget text </th>
		<th> flaw type </th>
		<th> info </th>
		<th> hint </th>
	</tr>
	<tr>
		<td> id/name </td>
		<td> android.widget.EditText </td>
		<td> Station name </td>
		<td> SIZE </td>
		<td> 395,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/url </td>
		<td> android.widget.EditText </td>
		<td> Station url </td>
		<td> SIZE </td>
		<td> 395,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/play </td>
		<td> android.widget.RadioButton </td>
		<td> Play </td>
		<td> SIZE </td>
		<td> 62,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/stop </td>
		<td> android.widget.RadioButton </td>
		<td> Stop </td>
		<td> SIZE </td>
		<td> 65,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pause </td>
		<td> android.widget.RadioButton </td>
		<td> Pause </td>
		<td> SIZE </td>
		<td> 76,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/resume </td>
		<td> android.widget.RadioButton </td>
		<td> Resume </td>
		<td> SIZE </td>
		<td> 89,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/name </td>
		<td> android.widget.EditText </td>
		<td> Station name </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/url </td>
		<td> android.widget.EditText </td>
		<td> Station url </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity HelpActivity

<table border='1'>
	<tr>
		<th> widget id </th>
		<th> widget type </th>
		<th> widget text </th>
		<th> flaw type </th>
		<th> info </th>
		<th> hint </th>
	</tr>
	<tr>
		<td> id/help </td>
		<td> android.widget.TextView </td>
		<td> Shorty##Create shortcuts for Intent Radio. ##Create shortcuts##The display shows fields for the name and url of the radio station. Fill in the fields and touch the Create button to create the shortcut. The Cancel button will close the display. The Lookup button on the toolbar will open the Lookup display. ##Look up stations##The lookup display shows the same fields which may be filled in by selecting an item on the list or using the keyboard. The Add button will add an entry. The Remove button will remove the selected entry. ##Play stations##The Select button will close the display and return. The toolbar buttons may be used to play- stop- pause or resume the selected station on Intent Radio directly. ##Save and Restore##The Save and Restore items on the menu may be used to save and restore the current list of stations. The list location is Shorty/entries.json. This folder is accessible from a file manager or a connected PC. The list is in JSON format. ##Import##The Import item prompts for a file- default extras.csv in the same location. You may change the name and/or location. This file should be in CSV format- which may be saved from a spreadsheet. If found the entries will be added to the list. The function will not add duplicate entries that are already in the list- but will add duplicates in the file itself. ##More Information##The shortcuts use Shorty in the background- so will no longer work if Shorty is uninstalled. Shorty will not create shortcuts if Intent Radio is not installed. ##The source code is on Github. Please report issues on the Github issues page. ##Example extras file##"BBC Sussex"-"http://open.live.bbc.co.uk/mediaselector/5/select/version/2.0/mediaset/http-icy-mp3-a/vpid/bbc_radio_sussex/format/pls.pls"#"Splash FM"-"http://s3.xrad.io:8096/listen.pls"# </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
</table>


#### Activity com.android.browserBrowserActivity

<table border='1'>
	<tr>
		<th> widget id </th>
		<th> widget type </th>
		<th> widget text </th>
		<th> flaw type </th>
		<th> info </th>
		<th> hint </th>
	</tr>
	<tr>
		<td> id/name </td>
		<td> android.widget.EditText </td>
		<td> BBC Radio 1 </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/url </td>
		<td> android.widget.EditText </td>
		<td> http://www.listenlive.eu/bbcradio1.m3u </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity PathActivity

<table border='1'>
	<tr>
		<th> widget id </th>
		<th> widget type </th>
		<th> widget text </th>
		<th> flaw type </th>
		<th> info </th>
		<th> hint </th>
	</tr>
	<tr>
		<td> id/path </td>
		<td> android.widget.EditText </td>
		<td> Shorty/extras.csv </td>
		<td> SIZE </td>
		<td> 288,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity LookupActivity

<table border='1'>
	<tr>
		<th> widget id </th>
		<th> widget type </th>
		<th> widget text </th>
		<th> flaw type </th>
		<th> info </th>
		<th> hint </th>
	</tr>
	<tr>
		<td> id/lu_name </td>
		<td> android.widget.EditText </td>
		<td> Station name </td>
		<td> SIZE </td>
		<td> 395,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/lu_url </td>
		<td> android.widget.EditText </td>
		<td> Station url </td>
		<td> SIZE </td>
		<td> 395,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/lu_name </td>
		<td> android.widget.EditText </td>
		<td> Station name </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/lu_url </td>
		<td> android.widget.EditText </td>
		<td> Station url </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> BBC Radio 4 </td>
		<td> CONTRAST </td>
		<td> 4.048577032340481 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> BBC Radio 2 </td>
		<td> SIZE </td>
		<td> 395,23 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>

