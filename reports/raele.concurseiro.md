---
layout: default
title: MATE Report for Concurseiro
---

### Flaws in Concurseiro (raele.concurseiro)


#### Activity ui.activity.TopicSelectionActivity

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
		<td> id/TopicSelection_TopicList </td>
		<td> android.widget.ListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/custom </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 358,38 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/custom </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/alertTitle </td>
		<td> android.widget.TextView </td>
		<td> Assunto </td>
		<td> CONTRAST </td>
		<td> 2.168716292881811 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/custom-child-0android.widget.EditText </td>
		<td> android.widget.EditText </td>
		<td> prepanic </td>
		<td> CONTRAST </td>
		<td> 2.9963775951615235 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/message </td>
		<td> android.widget.TextView </td>
		<td> Qual assunto você estudou? </td>
		<td> CONTRAST </td>
		<td> 2.168716292881811 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity ui.activity.RecordStudyActivity

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
		<td> id/RecordStudy_StudyList </td>
		<td> android.widget.ListView </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 379,0 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/RecordStudy_AddStudy </td>
		<td> android.widget.Button </td>
		<td> + </td>
		<td> CONTRAST </td>
		<td> 1.373295049118723 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/Study_Time </td>
		<td> android.widget.EditText </td>
		<td> 1 </td>
		<td> SIZE </td>
		<td> 63,28 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/RecordStudy_StudyList </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> Duplicate clickable bounds </td>
		<td>  </td>
		<td> View has same bounds as another view (likely a descendent) </td>
	</tr>
	<tr>
		<td> id/Study_Time </td>
		<td> android.widget.EditText </td>
		<td> 1 </td>
		<td> CONTRAST </td>
		<td> 1.385770632336024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
	</tr>
	<tr>
	</tr>
	<tr>
		<td> androidid/alertTitle </td>
		<td> android.widget.TextView </td>
		<td> Aviso </td>
		<td> CONTRAST </td>
		<td> 2.168716292881811 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/SubjectSpinner_Name </td>
		<td> android.widget.TextView </td>
		<td> Escolha uma matéria </td>
		<td> CONTRAST </td>
		<td> 1.0088986350087497 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

