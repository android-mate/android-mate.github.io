---
layout: default
title: MATE Report for mGerrit
---

### Flaws in mGerrit (com.jbirdvegas.mgerrit)


#### Activity activities.GerritControllerActivity

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
		<td> id/tool_bar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 36,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pager_header </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,19 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_cards </td>
		<td> android.widget.ListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,571 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/refine_search_container </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_commit_owner </td>
		<td> android.widget.TextView </td>
		<td> doc HD </td>
		<td> SIZE </td>
		<td> 64,27 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_settings </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 44,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 20,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/tool_bar-child-2android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.3231230535045992 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_header-child-2android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Merged </td>
		<td> CONTRAST </td>
		<td> 2.5142725384493976 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.1315743843019344 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_last_updated </td>
		<td> android.widget.TextView </td>
		<td> 08:40 PM </td>
		<td> CONTRAST </td>
		<td> 3.6900293509358773 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_project_name </td>
		<td> android.widget.TextView </td>
		<td> AICP/build </td>
		<td> CONTRAST </td>
		<td> 1.7625598210034286 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_settings </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.3231230535045992 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/header </td>
		<td> android.widget.TextView </td>
		<td> Sunday- September 17 2017 </td>
		<td> CONTRAST </td>
		<td> 1.3713058806238527 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tool_bar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.689276817599431 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tool_bar-child-1android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> AOSP </td>
		<td> CONTRAST </td>
		<td> 1.5477999070098158 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/txtHeaderLine1 </td>
		<td> android.widget.TextView </td>
		<td> AOSP </td>
		<td> CONTRAST </td>
		<td> 2.276098239349868 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/material_drawer_name </td>
		<td> android.widget.TextView </td>
		<td> View Changes </td>
		<td> CONTRAST </td>
		<td> 2.101121873377451 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_title </td>
		<td> android.widget.TextView </td>
		<td> Fix extracting 32-bit uuid error via calling method uuidToBytes </td>
		<td> CONTRAST </td>
		<td> 1.1377769909555424 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> View change details </td>
		<td> CONTRAST </td>
		<td> 1.2647322470553344 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/txtRefineSearchKeywordCount </td>
		<td> android.widget.TextView </td>
		<td> (1 filters active) </td>
		<td> CONTRAST </td>
		<td> 1.9407754808254007 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_header-child-0android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Review </td>
		<td> CONTRAST </td>
		<td> 2.5142725384493976 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/refine_search_wrapper-child-0android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Refine Your Search </td>
		<td> CONTRAST </td>
		<td> 2.5767501402854087 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/custom-child-0android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Review </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/custom-child-2android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Merged </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button3 </td>
		<td> android.widget.Button </td>
		<td> Gerrit help </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td>    Search #no or subject </td>
		<td> SIZE </td>
		<td> 355,36 </td>
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
		<td>    Search #no or subject </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/search_close_btn </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.3845378872067404 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td>    Search #no or subject </td>
		<td> CONTRAST </td>
		<td> 3.927903893440724 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs </td>
		<td> android.support.v4.view.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_header-child-1android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Abandoned </td>
		<td> CONTRAST </td>
		<td> 4.269827882774955 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_commit_owner </td>
		<td> android.widget.TextView </td>
		<td> Huji </td>
		<td> CONTRAST </td>
		<td> 3.6900293509358773 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity activities.PrefsActivity

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
		<td> Services </td>
		<td> SIZE </td>
		<td> 411,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/summary </td>
		<td> android.widget.TextView </td>
		<td> https://gerrit.omnirom.org/ </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Services </td>
		<td> CONTRAST </td>
		<td> 2.598744778475756 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/list </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,25 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity activities.ProjectsList

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
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> RunningStat </td>
		<td> SIZE </td>
		<td> 395,17 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search projects </td>
		<td> SIZE </td>
		<td> 339,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search projects </td>
		<td> CONTRAST </td>
		<td> 3.943775821870012 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search projects </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
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
		<td> androidid/text1 </td>
		<td> android.widget.TextView </td>
		<td> 3d2png </td>
		<td> CONTRAST </td>
		<td> 1.9428444088106975 </td>
		<td> Contrast ratio should be at least 4.5 </td>
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
		<td> id/tool_bar </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 36,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/pager_header </td>
		<td> android.widget.TextView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,19 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_cards </td>
		<td> android.widget.ListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,571 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/refine_search_container </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_commit_owner </td>
		<td> android.widget.TextView </td>
		<td> Jae Shin </td>
		<td> SIZE </td>
		<td> 64,27 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_settings </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 44,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/tool_bar-child-2android.widget.ImageView </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.3231230535045992 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/pager_header-child-2android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Merged </td>
		<td> CONTRAST </td>
		<td> 2.5142725384493976 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_last_updated </td>
		<td> android.widget.TextView </td>
		<td> 12:14 AM </td>
		<td> CONTRAST </td>
		<td> 2.4632730504708715 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_project_name </td>
		<td> android.widget.TextView </td>
		<td> platform/frameworks/native </td>
		<td> CONTRAST </td>
		<td> 3.9494396480491156 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_settings </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.3231230535045992 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/header </td>
		<td> android.widget.TextView </td>
		<td> Sunday- September 17 2017 </td>
		<td> CONTRAST </td>
		<td> 1.3493331394335433 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity activities.RefineSearchActivity

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
		<td> id/lv_search_categories </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 395,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search #no or subject </td>
		<td> SIZE </td>
		<td> 339,36 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search #no or subject </td>
		<td> CONTRAST </td>
		<td> 3.943775821870012 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/search_src_text </td>
		<td> android.widget.EditText </td>
		<td> Search #no or subject </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/txtCategoryName </td>
		<td> android.widget.TextView </td>
		<td> Branch </td>
		<td> CONTRAST </td>
		<td> 2.9209757321164957 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> SIZE </td>
		<td> 358,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/text1 </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Clear </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Apply </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/autoComplete </td>
		<td> android.widget.EditText </td>
		<td> Ting Zheng <ting.zheng@mediatek.com> </td>
		<td> SIZE </td>
		<td> 358,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/autoComplete </td>
		<td> android.widget.EditText </td>
		<td> Ting Zheng <ting.zheng@mediatek.com> </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/txtSearchDate </td>
		<td> android.widget.TextView </td>
		<td> Monday- September 18 2017 </td>
		<td> SIZE </td>
		<td> 203,21 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/txtSearchTime </td>
		<td> android.widget.TextView </td>
		<td> 01:06 </td>
		<td> SIZE </td>
		<td> 40,21 </td>
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
		<td> androidid/hours </td>
		<td> android.widget.TextView </td>
		<td> 00 </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/separator </td>
		<td> android.widget.TextView </td>
		<td> : </td>
		<td> CONTRAST </td>
		<td> 2.4719770612533094 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/minutes </td>
		<td> android.widget.TextView </td>
		<td> 00 </td>
		<td> CONTRAST </td>
		<td> 2.4719770612533094 </td>
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
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/date_picker_header_date </td>
		<td> android.widget.TextView </td>
		<td> Mon- Sep 18 </td>
		<td> CONTRAST </td>
		<td> 3.430560191498449 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/day_picker_view_pager </td>
		<td> com.android.internal.widget.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-0android.view.View </td>
		<td> android.view.View </td>
		<td> 5 </td>
		<td> CONTRAST </td>
		<td> 1.2390514843934626 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-1android.view.View </td>
		<td> android.view.View </td>
		<td> 12 </td>
		<td> CONTRAST </td>
		<td> 1.2390514843934626 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-2android.view.View </td>
		<td> android.view.View </td>
		<td> 19 </td>
		<td> CONTRAST </td>
		<td> 2.265648857193612 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-3android.view.View </td>
		<td> android.view.View </td>
		<td> 26 </td>
		<td> CONTRAST </td>
		<td> 2.104609025717842 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-10android.view.View </td>
		<td> android.view.View </td>
		<td> 11 </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-16android.view.View </td>
		<td> android.view.View </td>
		<td> 17 </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-17android.view.View </td>
		<td> android.view.View </td>
		<td> 18 </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/month_view-child-4android.view.View </td>
		<td> android.view.View </td>
		<td> 29 </td>
		<td> CONTRAST </td>
		<td> 2.104609025717842 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/autoComplete </td>
		<td> android.widget.EditText </td>
		<td> Search… </td>
		<td> CONTRAST </td>
		<td> 2.5744467644518627 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity activities.PatchSetViewerActivity

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
		<td> id/commit_cards </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 0,603 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 4.145460935624636 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_project_name </td>
		<td> android.widget.TextView </td>
		<td> platform/cts </td>
		<td> CONTRAST </td>
		<td> 3.8448810049535913 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_starred </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.4844104385898933 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/expand_activities_button </td>
		<td> android.widget.FrameLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 56,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/default_activity_button </td>
		<td> android.widget.FrameLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 56,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_commit_owner </td>
		<td> android.widget.TextView </td>
		<td> Ting Zheng </td>
		<td> SIZE </td>
		<td> 64,35 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_project_name </td>
		<td> android.widget.TextView </td>
		<td> platform/frameworks/base </td>
		<td> SIZE </td>
		<td> 269,19 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_starred </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_wrapper </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 7,99 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_card_committer_image </td>
		<td> android.widget.ImageView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 28,48 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/commit_cards </td>
		<td> android.widget.ExpandableListView </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> id/header </td>
		<td> android.widget.TextView </td>
		<td> Properties </td>
		<td> CONTRAST </td>
		<td> 1.363683159598655 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tabs </td>
		<td> android.support.v4.view.ViewPager </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.4903231307620617 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/tool_bar-child-0android.widget.ImageButton </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 3.8308200809188357 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/prop_card_change_id </td>
		<td> android.widget.TextView </td>
		<td> Ic08c00b15b1fd3d50f88711a7d4057dd13d1d850 </td>
		<td> CONTRAST </td>
		<td> 4.059746003770842 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/prop_card_created </td>
		<td> android.widget.TextView </td>
		<td> September 14- 2017 at 12:07:26 AM </td>
		<td> CONTRAST </td>
		<td> 4.059746003770842 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/prop_card_last_update </td>
		<td> android.widget.TextView </td>
		<td> September 18- 2017 at 12:55:54 AM </td>
		<td> CONTRAST </td>
		<td> 4.059746003770842 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/prop_card_branch </td>
		<td> android.widget.TextView </td>
		<td> master </td>
		<td> CONTRAST </td>
		<td> 3.9494396480491156 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/prop_card_topic </td>
		<td> android.widget.TextView </td>
		<td> bug/1717144 </td>
		<td> CONTRAST </td>
		<td> 4.059746003770842 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity activities.SigninActivity

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
		<td> id/txtUser </td>
		<td> android.widget.EditText </td>
		<td> Username </td>
		<td> SIZE </td>
		<td> 395,43 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/txtPass </td>
		<td> android.widget.EditText </td>
		<td> Password </td>
		<td> SIZE </td>
		<td> 395,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/txtSigninHelp </td>
		<td> android.widget.TextView </td>
		<td> This Gerrit is protected and requires you to sign in before you can view changes. If you do not know your username/password- you can generate one on your account settings page. </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/txtUser </td>
		<td> android.widget.EditText </td>
		<td> Username </td>
		<td> CONTRAST </td>
		<td> 1.9502150416025161 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/txtUser </td>
		<td> android.widget.EditText </td>
		<td> Username </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/txtPass </td>
		<td> android.widget.EditText </td>
		<td> Password </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/txtPass </td>
		<td> android.widget.EditText </td>
		<td> Password </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/btnSignin </td>
		<td> android.widget.Button </td>
		<td> Error </td>
		<td> CONTRAST </td>
		<td> 2.912836840606881 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity activities.GerritSwitcher

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
		<td> id/lv_gerrit_switcher </td>
		<td> android.widget.RelativeLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 395,46 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/txtGerritName </td>
		<td> android.widget.TextView </td>
		<td> AICP </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/chk_gerrit_selected </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.9502150416025161 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/chk_gerrit_selected </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/chk_gerrit_selected </td>
		<td> android.widget.RadioButton </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 32,89 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add_team_name_edittext </td>
		<td> android.widget.EditText </td>
		<td> New Gerrit team name </td>
		<td> SIZE </td>
		<td> 351,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add_team_url_edittext </td>
		<td> android.widget.EditText </td>
		<td> https:// </td>
		<td> SIZE </td>
		<td> 351,44 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/add_team_name_edittext </td>
		<td> android.widget.EditText </td>
		<td> New Gerrit team name </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/add_team_name_edittext </td>
		<td> android.widget.EditText </td>
		<td> New Gerrit team name </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/add_team_url_edittext </td>
		<td> android.widget.EditText </td>
		<td> https:// </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/add_team_url_edittext </td>
		<td> android.widget.EditText </td>
		<td> https:// </td>
		<td> DUPLICATE LABEL </td>
		<td>  </td>
		<td> View has the same label as another view </td>
	</tr>
	<tr>
		<td> id/txtGerritURL </td>
		<td> android.widget.TextView </td>
		<td> http://gerrit.aicp-rom.com/ </td>
		<td> CONTRAST </td>
		<td> 4.284813567788539 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

