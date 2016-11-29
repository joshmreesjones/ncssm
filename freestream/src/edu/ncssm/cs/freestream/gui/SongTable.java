package edu.ncssm.cs.freestream.gui;

import java.awt.Component;

import javax.swing.border.Border;
import javax.swing.border.EmptyBorder;
import javax.swing.JComponent;
import javax.swing.JTable;
import javax.swing.ListSelectionModel;
import javax.swing.table.DefaultTableCellRenderer;
import javax.swing.table.TableCellRenderer;

/**
 * An implementation of JTable specific to displaying songs in a table.
 * 
 * @author Josh Rees-Jones
 */
public class SongTable extends JTable {
	/**
	 * Constructs a SongTable with the specified SongTableModel.
	 * 
	 * @param model the SongTableModel to be used with this SongTable
	 */
	public SongTable(SongTableModel model) {
		this.setModel(model);
		this.setShowVerticalLines(false);
		this.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		this.setDefaultRenderer(String.class, new ProxyCellRenderer(this.getDefaultRenderer(String.class)));
	}

	private static class ProxyCellRenderer implements TableCellRenderer {
		protected static final Border DEFAULT_BORDER = new EmptyBorder(0, 0, 0, 0);
		private TableCellRenderer renderer;

		public ProxyCellRenderer(TableCellRenderer renderer) {
			this.renderer = renderer;
		}

		@Override
		public Component getTableCellRendererComponent(JTable table,
													   Object value,
													   boolean isSelected,
													   boolean hasFocus,
													   int row,
													   int column) {
			System.out.println("getTableCellRendererComponent() called");
			Component component = renderer.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);

			if (component instanceof JComponent) {
				((JComponent) component).setBorder(DEFAULT_BORDER);
			}
			
			return component;
		}
	}
}
