---
layout: default
title: MATE Report for CIDR Calculator
---

### Flaws in CIDR Calculator (us.lindanrandy.cidrcalculator)


#### Activity Preferences

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
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Preferences </td>
		<td> SIZE </td>
		<td> 411,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/list </td>
		<td> android.widget.ListView </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Auto Complete </td>
		<td> CONTRAST </td>
		<td> 2.6265604525055526 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/summary </td>
		<td> android.widget.TextView </td>
		<td> Use the history to auto complete the IP address. </td>
		<td> CONTRAST </td>
		<td> 1.973722359466373 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity CIDRCalculator

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
		<td> androidid/action_bar </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/ipaddress </td>
		<td> android.widget.EditText </td>
		<td> oversuds </td>
		<td> SIZE </td>
		<td> 188,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bitlength </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 222,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/subnetmask </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/keyboardview </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/ipaddress </td>
		<td> android.widget.EditText </td>
		<td> oversuds </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.CheckedTextView </td>
		<td> 255.255.252.0 </td>
		<td> SIZE </td>
		<td> 387,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.CheckedTextView </td>
		<td> /22 </td>
		<td> CONTRAST </td>
		<td> 1.0434884496936805 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity HistoryList

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
		<td> androidid/action_bar </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
	</tr>
</table>


#### Activity IPv6Calculator

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
		<td> id/keyboardview </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/ipv6address </td>
		<td> android.widget.EditText </td>
		<td> Put IP here </td>
		<td> SIZE </td>
		<td> 411,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/ipv6subnetmasks </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/ipv6address </td>
		<td> android.widget.EditText </td>
		<td> Put IP here </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.CheckedTextView </td>
		<td> ffff:ffff:ffff:ffff:ffc0:: = /74 </td>
		<td> SIZE </td>
		<td> 387,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity com.android.messagingui.conversationlist.ShareIntentActivity

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
		<td> androidid/action_bar </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/ipaddress </td>
		<td> android.widget.EditText </td>
		<td> Put IP here </td>
		<td> SIZE </td>
		<td> 188,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bitlength </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 222,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/subnetmask </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/ipaddress </td>
		<td> android.widget.EditText </td>
		<td> Put IP here </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity Converter

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
		<td> androidid/action_bar </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/converter_ipaddress </td>
		<td> android.widget.EditText </td>
		<td> Put IP here </td>
		<td> SIZE </td>
		<td> 188,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/ipbinary </td>
		<td> android.widget.EditText </td>
		<td> 00000000.00000000.00000000.00000000 </td>
		<td> SIZE </td>
		<td> 411,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/iphex </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 188,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/keyboardview </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/iphex </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/converter_ipaddress </td>
		<td> android.widget.EditText </td>
		<td> Put IP here </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
	</tr>
</table>

