class Playlist {
  constructor(songs) {
    this.songs = songs;
  }

  [Symbol.iterator]() {
    let index = 0;
    const songs = this.songs;
    return {
      next() {
        if (index >= songs.length) {
          return { done: true };
        }
        const value = songs[index];
        index += 1;
        return { value, done: false };
      },
    };
  }
}

function demo() {
  return [...new Playlist(["intro", "verse", "outro"])];
}

module.exports = { Playlist, demo };
