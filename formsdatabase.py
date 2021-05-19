"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if form.validate_on_submit():
        f = form.PlaylistForm
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'PlaylistForm', filename
        ))
        return redirect(url_for('index'))

    return render_template('upload.html', form=form)

class SongForm(FlaskForm):
    """Form for adding songs."""

    @app.route('/upload', methods=['GET', 'POST'])
def upload():
    if form.validate_on_submit():
        f = form.SongForm
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'SongForm', filename
        ))
        return redirect(url_for('index'))

    return render_template('upload.html', form=form)


def upload():
    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photos', filename
        ))
        return redirect(url_for('index'))

    return render_template('upload.html', form=form)


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
