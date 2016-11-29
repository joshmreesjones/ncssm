package edu.ncssm.cs.freestream.daemon;

import java.io.File;
import java.util.ArrayList;

import edu.ncssm.cs.freestream.daemon.PlaybackDaemon;
import edu.ncssm.cs.freestream.Song;

public class LocalFilesDaemon extends MusicDaemon {
	public ArrayList<Song> getSongs() {
		String home = System.getProperty("user.home");
		String separator = System.getProperty("file.separator");

		System.out.println(home + separator + "Music");

		return getSongs(new File(home + separator + "Music"));
	}

	public ArrayList<Song> getSongs(File location) {
		ArrayList<Song> songs = new ArrayList<Song>();

		// recursively find all .mp3 files
		for (File file : location.listFiles()) {
			if (file.isDirectory()) {
				songs.addAll(getSongs(file));
			} else {
				if (file.getName().endsWith(".mp3")) {
					songs.add(new Song(file));
				}
			}
		}

		return songs;
	}

	public void play(Song song) {
		
	}
}
