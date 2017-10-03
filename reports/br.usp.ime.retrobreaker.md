---
layout: default
title: MATE Report for Retro Breaker
---

### Flaws in Retro Breaker (br.usp.ime.retrobreaker)


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
		<td> id/levelSpinner </td>
		<td> android.widget.Spinner </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/soundEffectsCheckBox </td>
		<td> android.widget.CheckBox </td>
		<td> Enable sound effects </td>
		<td> SIZE </td>
		<td> 411,32 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> id/newGameButton </td>
		<td> android.widget.Button </td>
		<td> New game </td>
		<td> CONTRAST </td>
		<td> 1.8947143147843377 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/container-child-9android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Hard brick (need 2 hits to break it) </td>
		<td> CONTRAST </td>
		<td> 3.3417682087605907 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity GameActivity

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
		<td> id/highScore </td>
		<td> android.widget.TextView </td>
		<td> High score: 00000000 </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/score </td>
		<td> android.widget.TextView </td>
		<td> Score: 00000000 </td>
		<td> CONTRAST </td>
		<td> 1.9687325714873163 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/scoreMultiplier </td>
		<td> android.widget.TextView </td>
		<td> Multiplier: 1x </td>
		<td> CONTRAST </td>
		<td> 3.672578596072024 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/ready </td>
		<td> android.widget.TextView </td>
		<td> Ready? </td>
		<td> CONTRAST </td>
		<td> 1.9687325714873163 </td>
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
		<td> androidid/list </td>
		<td> android.support.v7.widget.RecyclerView </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 1.5911366887561762 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> New message </td>
		<td> CONTRAST </td>
		<td> 1.5911366887561762 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

