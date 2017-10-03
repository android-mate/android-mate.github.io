---
layout: default
title: MATE Report for Cat Avatar Generator
---

### Flaws in Cat Avatar Generator (com.agateau.catgenerator)


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
		<td> id/shareButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/infoButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/nameEditText </td>
		<td> android.widget.EditText </td>
		<td> Cat name </td>
		<td> CONTRAST </td>
		<td> 2.6767878242915786 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/nameEditText </td>
		<td> android.widget.EditText </td>
		<td> Cat name </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity android/com.android.internal.app.ChooserActivity

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
		<td> id/nameEditText </td>
		<td> android.widget.EditText </td>
		<td> Cat name </td>
		<td> CONTRAST </td>
		<td> 2.6767878242915786 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/nameEditText </td>
		<td> android.widget.EditText </td>
		<td> Cat name </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/resolver_list </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> id/shareButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/infoButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/shareButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.485959036877996 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/infoButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.485959036877996 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

