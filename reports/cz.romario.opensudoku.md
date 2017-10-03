---
layout: default
title: MATE Report for OpenSudoku
---

### Flaws in OpenSudoku (cz.romario.opensudoku)


#### Activity gui.SudokuListActivity

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
		<td> id/state </td>
		<td> android.widget.TextView </td>
		<td> Playing </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/time </td>
		<td> android.widget.TextView </td>
		<td> 00:32 </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/last_played </td>
		<td> android.widget.TextView </td>
		<td> Last played at 7:41 PM </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/created </td>
		<td> android.widget.TextView </td>
		<td> Created at 8:19 PM </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/note </td>
		<td> android.widget.EditText </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
</table>


#### Activity gui.SudokuPlayActivity

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
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Close </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/sudoku_board </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> 00:15 </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/switch_num_note </td>
		<td> android.widget.ImageButton </td>
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
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/alertTitle </td>
		<td> android.widget.TextView </td>
		<td> Help </td>
		<td> CONTRAST </td>
		<td> 2.687524230882976 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/message </td>
		<td> android.widget.TextView </td>
		<td> Keyboard controls##Use trackball to navigate to the desired cell and then press number on keyboard to fill in value. If you want to edit cell's note- press number with shift or alt.##Input modes##You can switch between several input modes using button in the lower right corner of the screen. You can also disable any input mode in game settings - it will be completely hidden then.##Popup input mode##Popup dialog is shown when you tap the cell. You can edit cell's content using this dialog.##Single Number input mode##First select any number button by pressing it. Then just tap on cells in which you want to have selected number filled.##Use Pencil button to toggle between cell's value and note editing.##Numpad input mode##Buttons act as a standard numeric keyboard.##Use Pencil button to toggle between cell's value and note editing.# </td>
		<td> CONTRAST </td>
		<td> 3.448051119963421 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity gui.GameSettingsActivity

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
		<td> Game Helpers </td>
		<td> SIZE </td>
		<td> 411,24 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/list </td>
		<td> android.widget.LinearLayout </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 411,3 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Fill in notes </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/seek_bar </td>
		<td> android.widget.SeekBar </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> OK </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity gui.SudokuEditActivity

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
		<td> id/sudoku_board </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> id/switch_num_note </td>
		<td> android.widget.ImageButton </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Edit sudoku </td>
		<td> CONTRAST </td>
		<td> 1.0 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity gui.FolderListActivity

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
		<td> androidid/custom </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> SIZE </td>
		<td> 366,14 </td>
		<td> Minimum touch target size is 48dp x 48dp.  </td>
	</tr>
	<tr>
		<td> androidid/custom </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> MISSING LABEL </td>
		<td>  </td>
		<td> View is missing label for a screen reader </td>
	</tr>
	<tr>
		<td> android.view.View- </td>
		<td> android.view.View </td>
		<td>  </td>
		<td> CONTRAST </td>
		<td> 1.8616116683257742 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button1 </td>
		<td> android.widget.Button </td>
		<td> Close </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/button2 </td>
		<td> android.widget.Button </td>
		<td> Cancel </td>
		<td> CONTRAST </td>
		<td> 2.573352682508454 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> androidid/title </td>
		<td> android.widget.TextView </td>
		<td> Import </td>
		<td> CONTRAST </td>
		<td> 2.4454370136463495 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>


#### Activity gui.SudokuExportActivity

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
		<td> androidid/content-child-2android.widget.TextView </td>
		<td> android.widget.TextView </td>
		<td> Directory </td>
		<td> CONTRAST </td>
		<td> 2.861179256933749 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
	<tr>
		<td> id/directory </td>
		<td> android.widget.EditText </td>
		<td> /sdcard/opensudoku </td>
		<td> CONTRAST </td>
		<td> 3.3394133551702163 </td>
		<td> Contrast ratio should be at least 4.5 </td>
	</tr>
</table>

