<header id="masthead" class="site-header" role="banner">
        <div class="container">
            <div class="site-branding">
                <?php if ( get_theme_mod('site_logo') ) : ?>
                    <a href="<?php echo esc_url( home_url( '/' ) ); ?>" title="<?php bloginfo('name'); ?>"><img src="<?php echo esc_url(get_theme_mod('site_logo')); ?>" alt="<?php bloginfo('name'); ?>" /></a>
                <?php else : ?>
                    <h1 class="site-title"><a href="<?php echo esc_url( home_url( '/' ) ); ?>" rel="home"><?php bloginfo( 'name' ); ?></a></h1>
                    <h2 class="site-description"><?php bloginfo( 'description' ); ?></h2>
                <?php endif; ?>
            </div>
        </div>
    </header><!-- #masthead -->