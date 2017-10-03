---
layout: default
title: MATE Report for Budget Watch
---

### Flaws in Budget Watch (protect.budgetwatch)


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
		<td> id/toolbar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> id/custom </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 363,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/custom </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> android.widget.Image- </td>
		<td> android.widget.Image </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.0215463515134533 </td>
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
		<td> id/expanded_menu </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
</table>


#### Activity ImportExportActivity

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
		<td> id/importOptionFixedButton </td>
		<td> android.widget.Button </td>
		<td> Use export location </td>
		<td> SIZE </td>
		<td> 379,14 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/exportFileFormatSpinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 293,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/importFileFormatSpinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 293,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/button3 </td>
		<td> android.widget.Button </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Send… </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity TransactionActivity

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
		<td> androidid/date_picker_header_year </td>
		<td> android.widget.TextView </td>
		<td> 2017 </td>
		<td> SIZE </td>
		<td> 301,37 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Sun- Sep 17 </td>
		<td> SIZE </td>
		<td> 179,45 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/month_view </td>
		<td> android.view.View </td>
		<td> 1 </td>
		<td> SIZE </td>
		<td> 44,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_year </td>
		<td> android.widget.TextView </td>
		<td> 2017 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Sun- Sep 17 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/day_picker_view_pager </td>
		<td> com.android.internal.widget.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-0android.view.View </td>
		<td> android.view.View </td>
		<td> 1 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-1android.view.View </td>
		<td> android.view.View </td>
		<td> 2 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-16android.view.View </td>
		<td> android.view.View </td>
		<td> 17 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Clean </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-2android.view.View </td>
		<td> android.view.View </td>
		<td> 3 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-9android.view.View </td>
		<td> android.view.View </td>
		<td> 10 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> 2015 </td>
		<td> SIZE </td>
		<td> 349,30 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> 2015 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-23android.view.View </td>
		<td> android.view.View </td>
		<td> 24 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-26android.view.View </td>
		<td> android.view.View </td>
		<td> 27 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-10android.view.View </td>
		<td> android.view.View </td>
		<td> 11 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-17android.view.View </td>
		<td> android.view.View </td>
		<td> 18 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/action_add </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 35,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> SIZE </td>
		<td> 264,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_close_btn </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> CONTRAST </td>
		<td> 2.974125705730848 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/search_close_btn </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.991576393109792 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-2android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.055563348850343 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-2android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Transactions </td>
		<td> CONTRAST </td>
		<td> 3.055563348850343 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-21android.view.View </td>
		<td> android.view.View </td>
		<td> 22 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-4android.view.View </td>
		<td> android.view.View </td>
		<td> 5 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-5android.view.View </td>
		<td> android.view.View </td>
		<td> 6 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-6android.view.View </td>
		<td> android.view.View </td>
		<td> 7 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-25android.view.View </td>
		<td> android.view.View </td>
		<td> 26 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity com.android.cameraCamera

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
		<td> id/toolbar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.77747118823737 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/budgetSpinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 310,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/nameEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/accountEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/valueEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/noteEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
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
		<td> androidid/list </td>
		<td> android.support.v7.widget.RecyclerView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
</table>


#### Activity BudgetActivity

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
		<td> androidid/date_picker_header_year </td>
		<td> android.widget.TextView </td>
		<td> 2017 </td>
		<td> SIZE </td>
		<td> 300,37 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Sun- Sep 17 </td>
		<td> SIZE </td>
		<td> 179,45 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/month_view </td>
		<td> android.view.View </td>
		<td> 1 </td>
		<td> SIZE </td>
		<td> 43,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_year </td>
		<td> android.widget.TextView </td>
		<td> 2017 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Sun- Sep 17 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/day_picker_view_pager </td>
		<td> com.android.internal.widget.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-16android.view.View </td>
		<td> android.view.View </td>
		<td> 17 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Set </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-0android.view.View </td>
		<td> android.view.View </td>
		<td> 1 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-1android.view.View </td>
		<td> android.view.View </td>
		<td> 2 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-6android.view.View </td>
		<td> android.view.View </td>
		<td> 7 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-13android.view.View </td>
		<td> android.view.View </td>
		<td> 14 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-21android.view.View </td>
		<td> android.view.View </td>
		<td> 22 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-5android.view.View </td>
		<td> android.view.View </td>
		<td> 6 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-10android.view.View </td>
		<td> android.view.View </td>
		<td> 11 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-17android.view.View </td>
		<td> android.view.View </td>
		<td> 18 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-20android.view.View </td>
		<td> android.view.View </td>
		<td> 21 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-22android.view.View </td>
		<td> android.view.View </td>
		<td> 23 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-18android.view.View </td>
		<td> android.view.View </td>
		<td> 19 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-19android.view.View </td>
		<td> android.view.View </td>
		<td> 20 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-23android.view.View </td>
		<td> android.view.View </td>
		<td> 24 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-24android.view.View </td>
		<td> android.view.View </td>
		<td> 25 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-25android.view.View </td>
		<td> android.view.View </td>
		<td> 26 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/day_picker_view_pager </td>
		<td> com.android.internal.widget.ViewPager </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 348,5 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/prev </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 48,15 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/next </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 48,15 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-9android.view.View </td>
		<td> android.view.View </td>
		<td> 10 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-11android.view.View </td>
		<td> android.view.View </td>
		<td> 12 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-12android.view.View </td>
		<td> android.view.View </td>
		<td> 13 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-14android.view.View </td>
		<td> android.view.View </td>
		<td> 15 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-15android.view.View </td>
		<td> android.view.View </td>
		<td> 16 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-28android.view.View </td>
		<td> android.view.View </td>
		<td> 29 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-7android.view.View </td>
		<td> android.view.View </td>
		<td> 8 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-8android.view.View </td>
		<td> android.view.View </td>
		<td> 9 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-2android.view.View </td>
		<td> android.view.View </td>
		<td> 3 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-3android.view.View </td>
		<td> android.view.View </td>
		<td> 4 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-4android.view.View </td>
		<td> android.view.View </td>
		<td> 5 </td>
		<td> CONTRAST </td>
		<td> 3.9984767707539985 </td>
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
		<td> androidid/prev </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-30android.view.View </td>
		<td> android.view.View </td>
		<td> 31 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-27android.view.View </td>
		<td> android.view.View </td>
		<td> 28 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-29android.view.View </td>
		<td> android.view.View </td>
		<td> 30 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> 2015 </td>
		<td> SIZE </td>
		<td> 348,30 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> 2015 </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity TransactionViewActivity

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
		<td> id/nameEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/accountEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/valueEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/noteEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/budgetSpinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 310,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.77747118823737 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/accountEdit </td>
		<td> android.widget.EditText </td>
		<td> filigree </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/content </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,47 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity permission.ui.GrantPermissionsActivity

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
		<td> id/permission_deny_button </td>
		<td> android.widget.Button </td>
		<td> Deny </td>
		<td> CONTRAST </td>
		<td> 3.2415605925446007 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/permission_allow_button </td>
		<td> android.widget.Button </td>
		<td> Allow </td>
		<td> CONTRAST </td>
		<td> 3.2415605925446007 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity BudgetViewActivity

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
		<td> id/valueEdit </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.77747118823737 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/budgetNameEdit </td>
		<td> android.widget.EditText </td>
		<td> Teloogoo </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/content </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,47 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/valueEdit </td>
		<td> android.widget.EditText </td>
		<td> Oeneus </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity SettingsActivity

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
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.3320882086652337 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

