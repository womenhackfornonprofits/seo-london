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
 * Lint our JavaScript for errors using ESLint
 */
gulp.task('js:lint', () => {
  // ESLint ignores files with "node_modules" paths.
  // So, it's best to have gulp ignore the directory as well.
  // Also, Be sure to return the stream from the task;
  // Otherwise, the task may end before the stream has finished.
  return gulp.src([
    'seolondon/js/**/*.js',
    '!node_modules/**'
  ])
  // eslint() attaches the lint output to the "eslint" property
  // of the file object so it can be used by other modules.
    .pipe($.eslint())
    // eslint.format() outputs the lint results to the console.
    // Alternatively use eslint.formatEach() (see Docs).
    .pipe($.eslint.format())
    // To have the process exit with an error code (1) on
    // lint error, return the stream and pipe to failAfterError last.
    .pipe($.eslint.failAfterError());
});

/**
 * Compile our JavaScript files using Babel and Uglify
 */
gulp.task('js:compile', ['js:lint'], () => {
  return gulp.src([
    'seolondon/js/main.js',
    'seolondon/js/**/*.js',
  ])
    .pipe($.sourcemaps.init())
    .pipe($.babel({
      presets: ['es2015']
    }))
    .pipe($.concat('scripts.min.js'))
    .pipe($.uglify({
      mangle: true,
      compress: true,
      preserveComments: 'license'
    }))
    .pipe($.sourcemaps.write('.'))
    .pipe(gulp.dest('seolondon/static/dist/temp/'));
});

/**
 * Concatenate our compiled JavaScript files with minified vendor files
 */
gulp.task('js:concat', ['js:compile'], () => {
  return gulp.src([
    'node_modules/jquery/dist/jquery.min.js',
    'seolondon/static/dist/semantic.min.js',
    'seolondon/vendor/unslider/js/unslider-min.js',
    'seolondon/static/dist/temp/scripts.min.js'
  ])
    .pipe($.sourcemaps.init({
      loadMaps: true
    }))
    .pipe($.concat('scripts.min.js'))
    .pipe($.sourcemaps.write('.'))
    .pipe(gulp.dest('seolondon/static/dist/'))
    .pipe($.livereload());
});

gulp.task('js', ['js:lint', 'js:compile', 'js:concat']);


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
        'seolondon/static/dist/temp/style.min.css',
        'seolondon/vendor/unslider/css/unslider.css',
        'seolondon/vendor/unslider/css/unslider-dots.css'
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
    gulp.watch('seolondon/js/**/*.js', {interval: 500}, ['js']);
    gulp.watch('**/*.html', () => $.livereload.reload());
    sequence('semantic:watch');  // NOTE: run semantic watch without callback
});

gulp.task('build', (done) => {
    sequence(['css', 'js'], done);
});

gulp.task('default', (done) => {
    sequence('build', ['semantic:watch', 'watch'], done);
});
