---
layout: default
title: MATE Report for OpenTasks
---

### Flaws in OpenTasks (org.dmfs.tasks)


#### Activity EditTaskActivity

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
		<td> id/content </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> SIZE </td>
		<td> 387,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/integer_choices_spinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 387,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,37 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/task_time_picker_remove </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/task_date_picker </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 192,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/task_time_picker </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 154,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.TextView </td>
		<td> 0% </td>
		<td> SIZE </td>
		<td> 22,290 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/task_date_picker </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/task_time_picker </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/task_time_picker_remove </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/task_list_account_name </td>
		<td> android.widget.TextView </td>
		<td> Local </td>
		<td> CONTRAST </td>
		<td> 2.8070664118795325 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> STATUS </td>
		<td> CONTRAST </td>
		<td> 2.3231230535045992 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/task_date_picker </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.8001756847703523 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/task_time_picker </td>
		<td> android.widget.Button </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.6900293509358773 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.3231230535045992 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/am_label </td>
		<td> android.widget.CheckedTextView </td>
		<td> AM </td>
		<td> SIZE </td>
		<td> 24,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/pm_label </td>
		<td> android.widget.CheckedTextView </td>
		<td> PM </td>
		<td> SIZE </td>
		<td> 24,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/hours </td>
		<td> android.widget.TextView </td>
		<td> 12 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/separator </td>
		<td> android.widget.TextView </td>
		<td> : </td>
		<td> CONTRAST </td>
		<td> 2.555496376450409 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/minutes </td>
		<td> android.widget.TextView </td>
		<td> 00 </td>
		<td> CONTRAST </td>
		<td> 2.555496376450409 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/am_label </td>
		<td> android.widget.CheckedTextView </td>
		<td> AM </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/pm_label </td>
		<td> android.widget.CheckedTextView </td>
		<td> PM </td>
		<td> CONTRAST </td>
		<td> 2.555496376450409 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_year </td>
		<td> android.widget.TextView </td>
		<td> 2017 </td>
		<td> SIZE </td>
		<td> 240,37 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Mon- Sep 18 </td>
		<td> SIZE </td>
		<td> 189,45 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/month_view </td>
		<td> android.view.View </td>
		<td> 1 </td>
		<td> SIZE </td>
		<td> 35,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_year </td>
		<td> android.widget.TextView </td>
		<td> 2017 </td>
		<td> CONTRAST </td>
		<td> 3.8806237466228057 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Mon- Sep 18 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/day_picker_view_pager </td>
		<td> com.android.internal.widget.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-0android.view.View </td>
		<td> android.view.View </td>
		<td> 5 </td>
		<td> CONTRAST </td>
		<td> 1.8340649860805518 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-1android.view.View </td>
		<td> android.view.View </td>
		<td> 12 </td>
		<td> CONTRAST </td>
		<td> 3.6573664310763587 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-2android.view.View </td>
		<td> android.view.View </td>
		<td> 19 </td>
		<td> CONTRAST </td>
		<td> 1.8340649860805518 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-3android.view.View </td>
		<td> android.view.View </td>
		<td> 26 </td>
		<td> CONTRAST </td>
		<td> 1.6962811727546023 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-10android.view.View </td>
		<td> android.view.View </td>
		<td> 11 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-16android.view.View </td>
		<td> android.view.View </td>
		<td> 17 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-17android.view.View </td>
		<td> android.view.View </td>
		<td> 18 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-18android.view.View </td>
		<td> android.view.View </td>
		<td> 19 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-4android.view.View </td>
		<td> android.view.View </td>
		<td> 29 </td>
		<td> CONTRAST </td>
		<td> 1.0306059068447981 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/next </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-5android.view.View </td>
		<td> android.view.View </td>
		<td> 6 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-6android.view.View </td>
		<td> android.view.View </td>
		<td> 7 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> androidid/month_view-child-25android.view.View </td>
		<td> android.view.View </td>
		<td> 26 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-26android.view.View </td>
		<td> android.view.View </td>
		<td> 27 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-27android.view.View </td>
		<td> android.view.View </td>
		<td> 28 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-20android.view.View </td>
		<td> android.view.View </td>
		<td> 21 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-21android.view.View </td>
		<td> android.view.View </td>
		<td> 22 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-22android.view.View </td>
		<td> android.view.View </td>
		<td> 23 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/percentage_seek_bar </td>
		<td> android.widget.SeekBar </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/task_time_picker_remove </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.8886562859962863 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.EditText </td>
		<td> URL </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> id/integer_choice_item_text </td>
		<td> android.widget.TextView </td>
		<td> (GMT-02:00) Greenland </td>
		<td> CONTRAST </td>
		<td> 1.892895964946571 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/task_list_name </td>
		<td> android.widget.TextView </td>
		<td> My tasks </td>
		<td> CONTRAST </td>
		<td> 3.9850652903439348 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.TextView </td>
		<td> 0% </td>
		<td> CONTRAST </td>
		<td> 3.6900293509358773 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity com.google.android.apps.maps/com.google.android.maps.MapsActivity

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
		<td> id/toolbar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/icon </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 36,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.TextView </td>
		<td> in process </td>
		<td> SIZE </td>
		<td> 82,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add_item </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 88,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 36,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.EditText </td>
		<td> lid </td>
		<td> SIZE </td>
		<td> 278,21 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/icon </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.163423997495252 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.EditText </td>
		<td> lid </td>
		<td> CONTRAST </td>
		<td> 3.9494396480491156 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.EditText </td>
		<td> lid </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.4031225876110116 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity ViewTaskActivity

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
		<td> id/toolbar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/icon </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 36,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.TextView </td>
		<td> in process </td>
		<td> SIZE </td>
		<td> 82,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add_item </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 88,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> Mon- September 18- 2017- 12:00 AM </td>
		<td> SIZE </td>
		<td> 286,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 36,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.EditText </td>
		<td> reacclimate </td>
		<td> SIZE </td>
		<td> 278,21 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/icon </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.EditText </td>
		<td> reacclimate </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/checkbox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.163423997495252 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.EditText </td>
		<td> ireos </td>
		<td> CONTRAST </td>
		<td> 3.9494396480491156 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.4031225876110116 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/expanded_menu </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> id/toolbar_title </td>
		<td> android.widget.TextView </td>
		<td> linenman </td>
		<td> CONTRAST </td>
		<td> 0.8487075817865437 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.163423997495252 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 3.163423997495252 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/remove_item </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/remove_item </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/remove_item </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 4.0041069566148515 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> Mon- September 18- 2017- 1:24 AM </td>
		<td> CONTRAST </td>
		<td> 2.3400975722094053 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.TextView </td>
		<td> stonemint </td>
		<td> CONTRAST </td>
		<td> 3.9850652903439348 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.9850652903439348 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-2android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.9850652903439348 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/button_add_one_day </td>
		<td> android.widget.TextView </td>
		<td> +1 day </td>
		<td> SIZE </td>
		<td> 73,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/button_add_one_day </td>
		<td> android.widget.TextView </td>
		<td> +1 day </td>
		<td> CONTRAST </td>
		<td> 2.1295152833378332 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/button_add_one_hour </td>
		<td> android.widget.TextView </td>
		<td> +1 hour </td>
		<td> SIZE </td>
		<td> 79,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/button_add_one_hour </td>
		<td> android.widget.TextView </td>
		<td> +1 hour </td>
		<td> CONTRAST </td>
		<td> 2.52994487096179 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity TaskListActivity

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
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/list </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> androidid/list </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,555 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/toolbar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Tasks </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-0android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-1android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-2android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-3android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-4android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-5android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager </td>
		<td> android.support.v4.view.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.775880814644327 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.775880814644327 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Already Started </td>
		<td> CONTRAST </td>
		<td> 3.2226601534228987 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text2 </td>
		<td> android.widget.TextView </td>
		<td> 0 tasks </td>
		<td> CONTRAST </td>
		<td> 2.038523043192234 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search </td>
		<td> SIZE </td>
		<td> 299,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search </td>
		<td> CONTRAST </td>
		<td> 1.9687325714873163 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/quick_add_task </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/quick_add_task </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_close_btn </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> Local </td>
		<td> CONTRAST </td>
		<td> 2.038523043192234 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/quick_add_task </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.8742079183642906 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/task_list_spinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 256,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/input </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> SIZE </td>
		<td> 262,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.TextView </td>
		<td> Save </td>
		<td> SIZE </td>
		<td> 153,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.TextView </td>
		<td> Save and continue </td>
		<td> SIZE </td>
		<td> 153,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/edit </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/task_list_name </td>
		<td> android.widget.TextView </td>
		<td> My tasks </td>
		<td> CONTRAST </td>
		<td> 3.368301581271026 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/input </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> CONTRAST </td>
		<td> 3.163423997495252 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/input </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.TextView </td>
		<td> Save </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/task_due_date </td>
		<td> android.widget.TextView </td>
		<td> Tomorrow </td>
		<td> CONTRAST </td>
		<td> 3.9494396480491156 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity ManageListActivity

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
		<td> androidid/input </td>
		<td> android.widget.EditText </td>
		<td> list name </td>
		<td> SIZE </td>
		<td> 247,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/input </td>
		<td> android.widget.EditText </td>
		<td> list name </td>
		<td> CONTRAST </td>
		<td> 3.5185868622496472 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/input </td>
		<td> android.widget.EditText </td>
		<td> list name </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.TextView </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.5185868622496472 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.TextView </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 3.5185868622496472 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button3 </td>
		<td> android.widget.TextView </td>
		<td> save </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity unkonwn

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
		<td> androidid/list </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> androidid/list </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,555 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/toolbar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Task progress </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-0android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-1android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-2android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-3android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-4android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs-child-5android.support.v7.app.ActionBar$Tab </td>
		<td> android.support.v7.app.ActionBar$Tab </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager </td>
		<td> android.support.v4.view.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.2226601534228987 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Almost done </td>
		<td> CONTRAST </td>
		<td> 3.2226601534228987 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text2 </td>
		<td> android.widget.TextView </td>
		<td> 0 tasks </td>
		<td> CONTRAST </td>
		<td> 2.038523043192234 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/floating_action_button </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.775880814644327 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity SyncSettingsActivity

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
		<td> id/btn_settings </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/action_bar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.5185868622496472 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/action_bar-child-1android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Displayed Lists </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/btn_settings </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.84518674838884 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity /org.dmfs.android.colorpicker.ColorPickerActivity

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
		<td> android.widget.GridView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 22,243 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pager_title_strip </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pager_title_strip </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/pager </td>
		<td> org.dmfs.android.view.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.12434068505182 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_title_strip-child-2android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_title_strip-child-5android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.875891530948359 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_title_strip-child-6android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.0250654124089245 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

