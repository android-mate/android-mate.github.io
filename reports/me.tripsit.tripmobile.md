---
layout: default
title: MATE Report for TripSit
---

### Flaws in TripSit (me.tripsit.tripmobile)


#### Activity /me.tripsit.mobile.settings.Settings

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
		<td> id/seek_cache </td>
		<td> android.widget.SeekBar </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/autocomplete_channel </td>
		<td> android.widget.EditText </td>
		<td> home </td>
		<td> SIZE </td>
		<td> 278,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity /me.tripsit.mobile.wiki.Wiki

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
	<tr>
		<td> androidid/content </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> androidid/content </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> android.widget.Button- </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.6213919207442387 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> android.widget.Image- </td>
		<td> android.widget.Image </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.9709257122141524 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> android.view.View- </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.405887226461303 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity /me.tripsit.mobile.chat.Chat

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
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> androidid/content </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/content </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 316,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> android.view.View- </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.3841461718450223 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> android.widget.Image- </td>
		<td> android.widget.Image </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.0088381905838484 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> android.widget.Button- </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.7383819305161423 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity /me.tripsit.mobile.factsheets.Factsheets

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
		<td> id/exlist_drugInfo </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 381,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/drugNameSearch </td>
		<td> android.widget.EditText </td>
		<td> Drug or alias </td>
		<td> SIZE </td>
		<td> 267,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/drugNameSearch </td>
		<td> android.widget.EditText </td>
		<td> Drug or alias </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity /me.tripsit.mobile.About

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
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
</table>


#### Activity /me.tripsit.mobile.Menu

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
		<td> id/btn_tripsitChannel </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_generalChat </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_factSheets </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_combinations </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_wiki </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_settings </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_contact </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/btn_about </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
</table>


#### Activity /me.tripsit.mobile.combination.CombinationActivity

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
		<td> id/input_first_drug </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 381,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/input_second_drug </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 381,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/input_first_drug </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/input_second_drug </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/txt_combo_content </td>
		<td> android.widget.TextView </td>
		<td> Failed to find drug (empty) - try a category or check the factsheets for spelling. </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

