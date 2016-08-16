'use strict';

const gulp = require('gulp');
const sequence = require('run-sequence').use(gulp);

const gulpLoadPlugins = require('gulp-load-plugins');
const $ = gulpLoadPlugins({
    rename: {
        'gulp-minify-css': 'cssmin'
    }
});

const semanticBuild = require('./semantic/tasks/build');
const semanticWatch = require('./semantic/tasks/watch');

/**
 * Stop sass and uglify errors from crashing the gulp watch
 * @param error
 */
function onError(error) {
    console.error(error);
    this.emit('end');
}

/**
 * Compile our SASS styles
 */
gulp.task('css:compile', () => {
    return gulp.src([
        'seolondon/sass/style.scss'
    ])
        .pipe($.sourcemaps.init())
        .pipe($.sass())
        .on('error', onError)
        .pipe($.autoprefixer('> 0.01%', 'ie 8'))
        .pipe($.csslint())
        .pipe($.cssmin())
        .pipe($.rename({
            extname: '.min.css'
        }))
        .pipe($.sourcemaps.write('.'))
        .pipe(gulp.dest('seolondon/static/dist/temp'));
});

/**
 * Concatenate our compiled SASS with minified vendor CSS files
 */
gulp.task('css:concat', ['css:compile'], () => {
    return gulp.src([
        'seolondon/static/dist/semantic.min.css',
        'seolondon/static/dist/temp/style.min.css'
    ])
        .pipe($.sourcemaps.init({
            loadMaps: true
        }))
        .pipe($.concat('styles.min.css'))
        .pipe($.sourcemaps.write('.'))
        .pipe(gulp.dest('seolondon/static/dist/'))
        .pipe($.filter('**/*.css'))
        .pipe($.livereload());
});

gulp.task('css', ['css:compile', 'css:concat']);

gulp.task('semantic:build', semanticBuild);
gulp.task('semantic:watch', semanticWatch);

/**
 * Watching for changes
 */
gulp.task('watch', () => {
    $.livereload.listen();
    gulp.watch('seolondon/static/dist/**/*.css', ['css']);
    gulp.watch('seolondon/sass/**/*.scss', ['css']);
    gulp.watch('**/*.html', () => $.livereload.reload());
    sequence('semantic:watch');  // NOTE: run semantic watch without callback
});

gulp.task('build', (done) => {
    sequence(['css'], done);
});

gulp.task('default', (done) => {
    sequence('build', ['semantic:watch', 'watch'], done);
});
