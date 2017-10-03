---
layout: default
title: MATE Report for Rocket Guardian
---

### Flaws in Rocket Guardian (atm.rocketguardian)


#### Activity AndroidLauncher

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
		<td> androidid/content </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
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
		<td> com.android.browserid/webview_wrapper </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> com.android.browserid/iconcombo </td>
		<td> android.widget.FrameLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 44,52 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> com.android.browserid/webview_wrapper </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> com.android.browserid/url </td>
		<td> android.widget.EditText </td>
		<td> https://touch.facebook.com/profile.php?id=100393240038469 </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> com.android.browserid/more </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.668142702867791 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> android.view.View- </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.1499806408645235 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> android.widget.Button- </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.7437589748116693 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

