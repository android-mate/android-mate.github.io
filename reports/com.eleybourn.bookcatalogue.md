---
layout: default
title: MATE Report for Book Catalogue
---

### Flaws in Book Catalogue (com.eleybourn.bookcatalogue)


#### Activity AdministrationFunctions

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
		<td> id/import_all_from_goodreads_label </td>
		<td> android.widget.TextView </td>
		<td> Import all from goodreads </td>
		<td> SIZE </td>
		<td> 406,34 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/send_books_to_goodreads_label </td>
		<td> android.widget.TextView </td>
		<td> Send books to goodreads </td>
		<td> SIZE </td>
		<td> 406,13 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/backup_catalogue_label </td>
		<td> android.widget.TextView </td>
		<td> Backup to Archive </td>
		<td> SIZE </td>
		<td> 406,37 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/restore_catalogue_label </td>
		<td> android.widget.TextView </td>
		<td> Import from Archive </td>
		<td> SIZE </td>
		<td> 406,10 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/backup_label </td>
		<td> android.widget.TextView </td>
		<td> Copy Database (for tech support) </td>
		<td> SIZE </td>
		<td> 406,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/export_label </td>
		<td> android.widget.TextView </td>
		<td> Export to CSV File </td>
		<td> SIZE </td>
		<td> 406,34 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity OtherPreferences

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
		<td> id/dynamic_properties </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 406,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/frame </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/frame </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/frame-child-0android.widget.CheckBox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.1806054384112215 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/name </td>
		<td> android.widget.TextView </td>
		<td> ADVANCED OPTIONS </td>
		<td> CONTRAST </td>
		<td> 3.46026509573834 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.6065137478764053 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity BookISBNSearch

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
		<td> id/author </td>
		<td> android.widget.EditText </td>
		<td> Author </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.EditText </td>
		<td> Title </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/isbn_del </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/asinCheckbox </td>
		<td> android.widget.CheckBox </td>
		<td> Allow ASIN </td>
		<td> SIZE </td>
		<td> 110,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/isbn </td>
		<td> android.widget.EditText </td>
		<td> ISBN </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/isbn_del </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.2281810092687648 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.EditText </td>
		<td> Arpa Con Alma Latina </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/isbn </td>
		<td> android.widget.EditText </td>
		<td> 0801655343425 </td>
		<td> SIZE </td>
		<td> 360,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/publisher </td>
		<td> android.widget.EditText </td>
		<td> Audio & Video Labs- Inc </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bookshelf </td>
		<td> android.widget.Button </td>
		<td> Default </td>
		<td> SIZE </td>
		<td> 391,20 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pages </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,46 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/row_img </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/row_img </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.905891104832624 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/author </td>
		<td> android.widget.Button </td>
		<td> lizary </td>
		<td> CONTRAST </td>
		<td> 2.362717598346001 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/series </td>
		<td> android.widget.Button </td>
		<td> Set Series… </td>
		<td> CONTRAST </td>
		<td> 2.362717598346001 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/publisher </td>
		<td> android.widget.EditText </td>
		<td> Audio & Video Labs- Inc </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/bookshelf </td>
		<td> android.widget.Button </td>
		<td> Default </td>
		<td> CONTRAST </td>
		<td> 1.8763991354177274 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pages </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity AdministrationAbout

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
		<td> id/sourcecode </td>
		<td> android.widget.TextView </td>
		<td> https://github.com/eleybourn/Book-Catalogue </td>
		<td> SIZE </td>
		<td> 406,28 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/contact1 </td>
		<td> android.widget.TextView </td>
		<td> eleybourn@gmail.com </td>
		<td> SIZE </td>
		<td> 406,28 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/contact2 </td>
		<td> android.widget.TextView </td>
		<td> philip.warner@rhyme.com.au </td>
		<td> SIZE </td>
		<td> 406,28 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/webpage </td>
		<td> android.widget.TextView </td>
		<td> https://wiki.github.com/eleybourn/Book-Catalogue/ </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/sourcecode </td>
		<td> android.widget.TextView </td>
		<td> https://github.com/eleybourn/Book-Catalogue </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/contact1 </td>
		<td> android.widget.TextView </td>
		<td> eleybourn@gmail.com </td>
		<td> CONTRAST </td>
		<td> 3.320218977084996 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/contact2 </td>
		<td> android.widget.TextView </td>
		<td> philip.warner@rhyme.com.au </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity filechooser.BackupChooser

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
		<td> id/file_name </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/file_name </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 406,43 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/row </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 398,30 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity BooksOnBookshelf

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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bookshelf_name </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 91,31 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bookshelf_down </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 54,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bookshelf_down </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/empty </td>
		<td> android.widget.TextView </td>
		<td> There are no books in this Bookshelf. Please add some using the menu at the bottom of this screen. </td>
		<td> CONTRAST </td>
		<td> 1.7065859540859585 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Hint </td>
		<td> CONTRAST </td>
		<td> 1.4072941377363481 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/confirm </td>
		<td> android.widget.Button </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 1.5045878959221466 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/menu </td>
		<td> android.widget.TextView </td>
		<td> Show more… </td>
		<td> SIZE </td>
		<td> 358,43 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/radio </td>
		<td> android.widget.RadioButton </td>
		<td> Author then Series </td>
		<td> SIZE </td>
		<td> 172,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/search_src_text </td>
		<td> android.widget.EditText </td>
		<td>    Search Author or Title </td>
		<td> SIZE </td>
		<td> 343,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/search_src_text </td>
		<td> android.widget.EditText </td>
		<td>    Search Author or Title </td>
		<td> CONTRAST </td>
		<td> 3.6410314886605417 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/search_src_text </td>
		<td> android.widget.EditText </td>
		<td>    Search Author or Title </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/search_close_btn </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 37,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/radio </td>
		<td> android.widget.RadioButton </td>
		<td> Language </td>
		<td> CONTRAST </td>
		<td> 1.3505908685015906 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/bookshelf_count </td>
		<td> android.widget.TextView </td>
		<td> (displaying 0 books) </td>
		<td> CONTRAST </td>
		<td> 1.036639111808363 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/row </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 406,43 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.TextView </td>
		<td> Arpa Con Alma Latina </td>
		<td> CONTRAST </td>
		<td> 1.524824437896998 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/select_dialog_listview </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
</table>


#### Activity BookEdit

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
		<td> id/row_img </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 41,41 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/isbn </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 360,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/publisher </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pages </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,19 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/list_price </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,39 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/row_img </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/isbn </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/publisher </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/pages </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/anthology </td>
		<td> android.widget.CheckBox </td>
		<td> Is this book an Anthology? </td>
		<td> SIZE </td>
		<td> 218,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/descriptionLabel </td>
		<td> android.widget.TextView </td>
		<td> Description (edit…) </td>
		<td> SIZE </td>
		<td> 391,41 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/format </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 343,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/genre </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/language </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/format_button </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/list_price </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/format </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/genre </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/language </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> id/year </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/month </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 66,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/day </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 54,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/year </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 62,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.CheckedTextView </td>
		<td> 25 </td>
		<td> SIZE </td>
		<td> 50,8 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.CheckedTextView </td>
		<td> 25 </td>
		<td> CONTRAST </td>
		<td> 1.5740574062458632 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/text </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.8388934157712187 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/bookshelf_dialog_root </td>
		<td> android.widget.CheckBox </td>
		<td> Default </td>
		<td> SIZE </td>
		<td> 304,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/read </td>
		<td> android.widget.CheckBox </td>
		<td> Have you read this book? </td>
		<td> SIZE </td>
		<td> 391,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/signed </td>
		<td> android.widget.CheckBox </td>
		<td> Has this book been signed </td>
		<td> SIZE </td>
		<td> 391,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/notes </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/location </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/rating </td>
		<td> android.widget.RatingBar </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/notes </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/location </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/bookshelf </td>
		<td> android.widget.Button </td>
		<td> Default </td>
		<td> SIZE </td>
		<td> 391,20 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/author </td>
		<td> android.widget.Button </td>
		<td> Set Authors… </td>
		<td> CONTRAST </td>
		<td> 2.362717598346001 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/isbn </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/series </td>
		<td> android.widget.Button </td>
		<td> Set Series… </td>
		<td> CONTRAST </td>
		<td> 2.362717598346001 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/publisher </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/date_published </td>
		<td> android.widget.Button </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 2.362717598346001 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/bookshelf </td>
		<td> android.widget.Button </td>
		<td> Default </td>
		<td> CONTRAST </td>
		<td> 2.362717598346001 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/dayLabel </td>
		<td> android.widget.TextView </td>
		<td> Day </td>
		<td> CONTRAST </td>
		<td> 1.424380207520071 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/minus </td>
		<td> android.widget.Button </td>
		<td> - </td>
		<td> CONTRAST </td>
		<td> 1.6296684243669957 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Share </td>
		<td> CONTRAST </td>
		<td> 3.1424701966289628 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/series </td>
		<td> android.widget.Button </td>
		<td> Set Series… </td>
		<td> SIZE </td>
		<td> 391,28 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pages </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/list_price </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/format </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/genre </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/language </td>
		<td> android.widget.EditText </td>
		<td> Not Set </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/anthology </td>
		<td> android.widget.CheckBox </td>
		<td> Is this book an Anthology? </td>
		<td> CONTRAST </td>
		<td> 1.524824437896998 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/row_img </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.804941830255196 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity goodreads.GoodreadsRegister

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
		<td> id/goodreads_url </td>
		<td> android.widget.TextView </td>
		<td> http://www.goodreads.com </td>
		<td> SIZE </td>
		<td> 406,33 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/goodreads_url </td>
		<td> android.widget.TextView </td>
		<td> http://www.goodreads.com </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity Bookshelf

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
		<td> androidid/select_dialog_listview </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
</table>


#### Activity AdministrationDonate

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
		<td> id/donate_url_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 406,46 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/donate_url_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
</table>


#### Activity EditSeriesList

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
		<td> id/series </td>
		<td> android.widget.EditText </td>
		<td> Series </td>
		<td> SIZE </td>
		<td> 264,33 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/series_num </td>
		<td> android.widget.EditText </td>
		<td> # </td>
		<td> SIZE </td>
		<td> 78,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add </td>
		<td> android.widget.Button </td>
		<td> Add </td>
		<td> SIZE </td>
		<td> 64,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/series </td>
		<td> android.widget.EditText </td>
		<td> Series </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/series </td>
		<td> android.widget.EditText </td>
		<td> Series </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/series_num </td>
		<td> android.widget.EditText </td>
		<td> # </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/series_num </td>
		<td> android.widget.EditText </td>
		<td> # </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity /org.acra.CrashReportDialog

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
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
</table>


#### Activity EditAuthorList

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
		<td> id/author </td>
		<td> android.widget.EditText </td>
		<td> Author </td>
		<td> SIZE </td>
		<td> 342,33 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add </td>
		<td> android.widget.Button </td>
		<td> Add </td>
		<td> SIZE </td>
		<td> 64,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/author </td>
		<td> android.widget.EditText </td>
		<td> Author </td>
		<td> CONTRAST </td>
		<td> 3.487096527395216 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/author </td>
		<td> android.widget.EditText </td>
		<td> Author </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
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
		<td> id/webpage </td>
		<td> android.widget.TextView </td>
		<td> https://wiki.github.com/eleybourn/Book-Catalogue/ </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/sourcecode </td>
		<td> android.widget.TextView </td>
		<td> https://github.com/eleybourn/Book-Catalogue </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/contact1 </td>
		<td> android.widget.TextView </td>
		<td> eleybourn@gmail.com </td>
		<td> CONTRAST </td>
		<td> 3.320218977084996 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/contact2 </td>
		<td> android.widget.TextView </td>
		<td> philip.warner@rhyme.com.au </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity booklist.BooklistStyleGroupsActivity

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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/row </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 406,21 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/present </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 44,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/row_details </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 323,47 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/present </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/present </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.9832124180928612 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity booklist.BooklistPreferencesActivity

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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/frame </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/dynamic_properties </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 401,41 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/frame </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/frame-child-0android.widget.CheckBox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.2347585101384202 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.6065137478764053 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity MainMenu

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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
</table>


#### Activity booklist.BooklistStylesActivity

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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/preferred </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/preferred </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 44,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> Clone style </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
</table>


#### Activity Help

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
		<td> id/helpinstructions </td>
		<td> android.widget.TextView </td>
		<td> Help </td>
		<td> SIZE </td>
		<td> 406,29 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/helppage </td>
		<td> android.widget.TextView </td>
		<td> https://github.com/eleybourn/Book-Catalogue/wiki/Help </td>
		<td> CONTRAST </td>
		<td> 3.340252881490264 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity BookshelfEdit

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
		<td> id/bookshelf </td>
		<td> android.widget.EditText </td>
		<td> Default </td>
		<td> SIZE </td>
		<td> 391,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/bookshelf </td>
		<td> android.widget.EditText </td>
		<td> Default </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>


#### Activity booklist.BooklistStylePropertiesActivity

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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/body </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 401,6 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/value </td>
		<td> android.widget.EditText </td>
		<td> Title first letter </td>
		<td> SIZE </td>
		<td> 386,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/frame </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/frame </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/value </td>
		<td> android.widget.EditText </td>
		<td> Title first letter </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/frame-child-0android.widget.CheckBox </td>
		<td> android.widget.CheckBox </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.2065846065986057 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/name </td>
		<td> android.widget.TextView </td>
		<td> Bookshelves </td>
		<td> CONTRAST </td>
		<td> 3.361159242503682 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/selector </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.6065137478764053 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/edit_button </td>
		<td> android.widget.Button </td>
		<td> Edit </td>
		<td> SIZE </td>
		<td> 48,4 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/edit_button </td>
		<td> android.widget.Button </td>
		<td> Edit </td>
		<td> CONTRAST </td>
		<td> 1.155234908006127 </td>
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
		<td> id/hide_hint_checkbox </td>
		<td> android.widget.CheckBox </td>
		<td> Do not show again </td>
		<td> SIZE </td>
		<td> 164,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
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
		<td> 182,40 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
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
		<td> com.android.browserid/url </td>
		<td> android.widget.EditText </td>
		<td> www.goodreads.com </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
</table>

