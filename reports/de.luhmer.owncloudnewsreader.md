---
layout: default
title: MATE Report for Nextcloud News
---

### Flaws in Nextcloud News (de.luhmer.owncloudnewsreader)


#### Activity NewsReaderListActivity

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
		<td> id/imgView_ShowPassword </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 43,56 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/cb_AllowAllSSLCertificates </td>
		<td> android.widget.CheckBox </td>
		<td> Disable Hostname Verification </td>
		<td> SIZE </td>
		<td> 331,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/username </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 331,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/password </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 331,45 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/text_input_password_toggle </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 31,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/edt_owncloudRootPath </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 331,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/username </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/password </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/text_input_password_toggle </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/edt_owncloudRootPath </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Sign in </td>
		<td> CONTRAST </td>
		<td> 3.40925118101649 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/password </td>
		<td> android.widget.EditText </td>
		<td> untopographically </td>
		<td> CONTRAST </td>
		<td> 3.40925118101649 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/ll_podcast_header </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 265,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/fl_playPausePodcastWrapper </td>
		<td> android.widget.FrameLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 64,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/btn_previousPodcastSlider </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,601 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/btn_playPausePodcastSlider </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 44,598 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/btn_nextPodcastSlider </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 40,601 </td>
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
		<td> id/list </td>
		<td> android.support.v7.widget.RecyclerView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/title </td>
		<td> android.widget.TextView </td>
		<td> Download more items </td>
		<td> CONTRAST </td>
		<td> 1.973722359466373 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/list_item_layout </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> id/toolbar-child-1android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> All unread items </td>
		<td> CONTRAST </td>
		<td> 1.047343550916453 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/toolbar-child-0android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.199565228153919 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/urlTextView </td>
		<td> android.widget.TextView </td>
		<td> ownCloud News </td>
		<td> CONTRAST </td>
		<td> 1.4386708810185902 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tV_feedsCount </td>
		<td> android.widget.TextView </td>
		<td> 0 </td>
		<td> CONTRAST </td>
		<td> 1.1650317621894808 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/username </td>
		<td> android.widget.EditText </td>
		<td> clime's </td>
		<td> CONTRAST </td>
		<td> 3.40925118101649 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tv_no_items_available </td>
		<td> android.widget.TextView </td>
		<td> No items here </td>
		<td> CONTRAST </td>
		<td> 1.773907974691296 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/edt_owncloudRootPath </td>
		<td> android.widget.EditText </td>
		<td> Sanetch </td>
		<td> CONTRAST </td>
		<td> 3.40925118101649 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/chg_row </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 358,3 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/chg_text </td>
		<td> android.widget.TextView </td>
		<td> Several other fixes and improvements </td>
		<td> SIZE </td>
		<td> 323,3 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/chg_textbullet </td>
		<td> android.widget.TextView </td>
		<td> • </td>
		<td> CONTRAST </td>
		<td> 2.089605528848847 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/chg_text </td>
		<td> android.widget.TextView </td>
		<td> Several other fixes and improvements </td>
		<td> CONTRAST </td>
		<td> 2.089605528848847 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/chg_rowheader </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 358,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
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
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Display </td>
		<td> SIZE </td>
		<td> 411,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/toolbar </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.CheckedTextView </td>
		<td> 2 </td>
		<td> CONTRAST </td>
		<td> 3.40925118101649 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.40925118101649 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity NewFeedActivity

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
		<td> id/et_feed_url </td>
		<td> android.widget.EditText </td>
		<td> Feed URL </td>
		<td> SIZE </td>
		<td> 379,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/sp_folder </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 379,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/et_feed_url </td>
		<td> android.widget.EditText </td>
		<td> Feed URL </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/btn_addFeed </td>
		<td> android.widget.Button </td>
		<td> Add feed </td>
		<td> CONTRAST </td>
		<td> 2.3116225600636957 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/btn_import_opml </td>
		<td> android.widget.Button </td>
		<td> Import OPML </td>
		<td> CONTRAST </td>
		<td> 2.3116225600636957 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/btn_export_opml </td>
		<td> android.widget.Button </td>
		<td> Export OPML </td>
		<td> CONTRAST </td>
		<td> 2.3116225600636957 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

