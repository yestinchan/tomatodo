module.exports = function(grunt) {

  //Force use of Unix newlines
  grunt.util.linefeed = '\n';


  // Project configuration.
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    banner : '/*! <%= pkg.name %>(v<%= pkg.version %>) <%= grunt.template.today("yyyy-mm-dd") %> */\n',
    jqueryCheck: 'if (typeof jQuery === "undefined") { throw new Error("jQuery required") }\n\n',
    dist: 'static',

    clean: {
      dist: ['<%= dist %>/js',
            '<%= dist %>/css',
            '<%= dist %>/fonts',
            '<%= dist %>/img']
    },

    coffee: {
        build: {
            options: {
                sourceMap: true
            }, 
            expand: true,
            flatten: true,
            cwd: 'coffee/', 
            src: ['*.coffee'], 
            dest: '<%= dist %>/js/', 
            ext: '.js'
        }
    },

    concat: {
      options: {
        banner: '<%= banner %><%= jqueryCheck %>',
        stripBanners: false
      },
      build: {
        src: [
          '<%= coffee.build.dest %>/*.js',
        ],
        dest: '<%= dist %>/js/<%= pkg.name %>.js'
      }
    },


    removelogging:{
      build:{
        src: ['<%= concat.build.dest %>'],
        dest: '<%= dist %>/js/<%= pkg.name %>.nolog.js',
        options:{}
      }
    },

    uglify: {
      options: {
        banner: '<%= banner %>',
        report: 'min'
      },
      build: {
        src: ['<%= removelogging.build.dest %>'],
        dest: '<%= dist %>/js/<%= pkg.name %>.min.js'
      }
    },

    recess: {
      options: {
        complie: true,
        banner: '<%= banner %>',
        noIDs: true,                 // Doesn't complain about using IDs in your stylesheets
        noJSPrefix: true,            // Doesn't complain about styling .js- prefixed classnames
        noOverqualifying: true,      // Doesn't complain about overqualified selectors (ie: div#foo.bar)
        noUnderscores: true,         // Doesn't complain about using underscores in your class names
        noUniversalSelectors: true,  // Doesn't complain about using the universal * selector
        strictPropertyOrder: false   // Complains if not strict property order
      },
      build: {
        src: ['less/main.less'],
        dest: '<%= dist %>/css/<%= pkg.name %>.css'
      },
      min: {
        options: {
          compress: true
        },
        src: ['less/main.less'],
        dest: '<%= dist %>/css/<%= pkg.name %>.min.css'
      }
    },

    copy: {
      fonts: {
        expand: true,
        src: ["fonts/*"],
        dest: '<%= dist %>/'
      },
      images: {
        expand: true,
        src: ["img/*"],
        dest: '<%= dist %>/'
      },
      libsjs: {
        expand: true,
        src: ["libs/js/*.js"],
        flatten: true,
        dest: "<%= dist %>/js/"
      },
      libscss: {
        expand: true,
        src: ["libs/css/*.css","libs/css/*.min.css"],
        flatten: true,
        dest: "<%= dist %>/css/"
      }
    }

  });

  // Load the plugin that provides the "uglify" task.

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-coffee');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-clean');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-remove-logging');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-recess');

  // JS distribution task.
  grunt.registerTask('dist-js', ['coffee' ,'concat', 'removelogging', 'uglify']);

  // CSS distribution task.
  grunt.registerTask('dist-css', ['recess']);

  // Fonts distribution task.
  grunt.registerTask('dist-fonts', ['copy:fonts']);

  // Images distribution task.
  grunt.registerTask('dist-images', ['copy:images']);

  // HTML distribution task.
  //grunt.registerTask('dist-htmls', ['copy:htmls']);

  grunt.registerTask('dist-libs-css', ['copy:libscss']);

  grunt.registerTask('dist-libs-js', ['copy:libsjs']);

  // libs distribution task.
  grunt.registerTask('dist-libs', ['dist-libs-css','dist-libs-js']);

  // Full distribution task.
  grunt.registerTask('dist', ['clean',  'dist-css', 'dist-js' , 'dist-images' , 'dist-fonts'  , 'dist-libs']);

  // Default task.
  grunt.registerTask('default', ['dist']);

};