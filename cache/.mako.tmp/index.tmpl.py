# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1601493088.935232
_enable_loop = True
_template_filename = '/home/nicky/.direnv/python-3.8.2/lib/python3.8/site-packages/nikola/data/themes/bootblog4/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header', 'before_content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        def before_content():
            return render_before_content(context._locals(__M_locals))
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        def content_header():
            return render_content_header(context._locals(__M_locals))
        math = _mako_get_namespace(context, 'math')
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'before_content'):
            context['self'].before_content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        index_file = _import_ns.get('index_file', context.get('index_file', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        permalink = _import_ns.get('permalink', context.get('permalink', UNDEFINED))
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        __M_writer('    ')
        __M_writer(str(math.math_styles_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        front_index_header = _import_ns.get('front_index_header', context.get('front_index_header', UNDEFINED))
        date_format = _import_ns.get('date_format', context.get('date_format', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        def content_header():
            return render_content_header(context)
        nextlink = _import_ns.get('nextlink', context.get('nextlink', UNDEFINED))
        posts = _import_ns.get('posts', context.get('posts', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        messages = _import_ns.get('messages', context.get('messages', UNDEFINED))
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        pagination = _mako_get_namespace(context, 'pagination')
        index_teasers = _import_ns.get('index_teasers', context.get('index_teasers', UNDEFINED))
        current_page = _import_ns.get('current_page', context.get('current_page', UNDEFINED))
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        page_links = _import_ns.get('page_links', context.get('page_links', UNDEFINED))
        prevlink = _import_ns.get('prevlink', context.get('prevlink', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        author_pages_generated = _import_ns.get('author_pages_generated', context.get('author_pages_generated', UNDEFINED))
        prev_next_links_reversed = _import_ns.get('prev_next_links_reversed', context.get('prev_next_links_reversed', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('        ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('        ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        __M_writer('    <div class="postindex">\n')
        for post in posts:
            __M_writer('            <article class="h-entry post-')
            __M_writer(str(post.meta('type')))
            __M_writer('" itemscope="itemscope" itemtype="http://schema.org/Article">\n            <header>\n                <h1 class="p-name entry-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" class="u-url">')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h1>\n                <div class="metadata">\n                    <p class="byline author vcard"><span class="byline-name fn" itemprop="author">\n')
            if author_pages_generated:
                __M_writer('                        <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                        ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('                    </span></p>\n            <p class="dateline">\n            <a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" rel="bookmark">\n            <time class="published dt-published" datetime="')
            __M_writer(str(post.formatted_date('webiso')))
            __M_writer('" itemprop="datePublished" title="')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('">')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('</time>\n')
            if post.updated and post.updated != post.date:
                __M_writer('                <span class="updated"> (')
                __M_writer(str(messages("updated")))
                __M_writer('\n                    <time class="dt-updated" datetime="')
                __M_writer(str(post.formatted_updated('webiso')))
                __M_writer('" itemprop="dateUpdated" title="')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.formatted_updated(date_format))))
                __M_writer('</time>)</span>\n')
            __M_writer('            </a>\n            </p>\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                        <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('                </div>\n            </header>\n')
            if index_teasers:
                __M_writer('                <div class="p-summary entry-summary">\n                    ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n                </div>\n')
            else:
                __M_writer('                <div class="e-content entry-content">\n                    ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n                </div>\n')
            __M_writer('            </article>\n')
        __M_writer('    </div>\n    ')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n    ')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n    ')
        __M_writer(str(math.math_scripts_ifposts(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def content_header():
            return render_content_header(context)
        kind = _import_ns.get('kind', context.get('kind', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n        ')
        __M_writer(str(feeds_translations.translation_link(kind)))
        __M_writer('\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_before_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        is_frontmost_index = _import_ns.get('is_frontmost_index', context.get('is_frontmost_index', UNDEFINED))
        featured = _import_ns.get('featured', context.get('featured', UNDEFINED))
        pagekind = _import_ns.get('pagekind', context.get('pagekind', UNDEFINED))
        len = _import_ns.get('len', context.get('len', UNDEFINED))
        def before_content():
            return render_before_content(context)
        url_replacer = _import_ns.get('url_replacer', context.get('url_replacer', UNDEFINED))
        theme_config = _import_ns.get('theme_config', context.get('theme_config', UNDEFINED))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        if 'main_index' in pagekind and is_frontmost_index and featured and (theme_config.get('featured_large') or theme_config.get('featured_small')):
            if theme_config.get('featured_on_mobile'):
                __M_writer('            <div class="d-block">\n')
            else:
                __M_writer('            <div class="d-none d-md-block">\n')
            if featured and theme_config.get('featured_large'):
                __M_writer('        <div class="jumbotron p-0 text-white rounded bg-dark">\n            <div class="row bootblog4-featured-jumbotron-row">\n                <div class="col-md-6 p-3 p-md-4 pr-0 h-md-250 bootblog4-featured-text">\n                    <h1 class="display-4 font-italic"><a class="text-white" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a></h1>\n')
                if featured[0].previewimage:
                    __M_writer('                            <div class="lead my-3 mb-0">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                    if theme_config.get('featured_large_image_on_mobile'):
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right">\n')
                    else:
                        __M_writer('                        <div class="col-md-6 p-0 h-md-250 text-right d-none d-md-block">\n')
                    __M_writer('                            <img class="bootblog4-featured-large-image" src="')
                    __M_writer(str(url_replacer(featured[0].permalink(), featured[0].previewimage, lang, 'full_path')))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n                        </div>\n')
                else:
                    __M_writer('                        <div class="lead my-3 mb-0">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                        </div>\n')
                __M_writer('            </div>\n        </div>\n')
            __M_writer('\n')
            if featured and theme_config.get('featured_small'):
                __M_writer('            <div class="row mb-2">\n')
                if len(featured) == 1:
                    __M_writer('                <div class="col-md-12">\n')
                else:
                    __M_writer('                <div class="col-md-6">\n')
                __M_writer('                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                __M_writer(str(featured[0].permalink()))
                __M_writer('">')
                __M_writer(str(featured[0].title()))
                __M_writer('</a>\n                           </h3>\n')
                if featured[0].previewimage:
                    __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                    __M_writer(str(url_replacer(featured[0].permalink(), featured[0].previewimage, lang, 'full_path')))
                    __M_writer('" alt="')
                    __M_writer(str(featured.pop(0).title()))
                    __M_writer('">\n')
                else:
                    __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                    __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                    __M_writer('</div>\n                           </div>\n')
                __M_writer('                    </div>\n                </div>\n\n')
                if featured:
                    __M_writer('               <div class="col-md-6">\n                    <div class="card flex-md-row mb-4 box-shadow h-md-250">\n                       <div class="card-body d-flex flex-column align-items-start">\n                           <h3 class="mb-0">\n                               <a class="text-dark" href="')
                    __M_writer(str(featured[0].permalink()))
                    __M_writer('">')
                    __M_writer(str(featured[0].title()))
                    __M_writer('</a>\n                           </h3>\n')
                    if featured[0].previewimage:
                        __M_writer('                               <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured[0].text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                               </div>\n                               <img class="card-img-right flex-auto d-none d-lg-block" src="')
                        __M_writer(str(url_replacer(featured[0].permalink(), featured[0].previewimage, lang, 'full_path')))
                        __M_writer('" alt="')
                        __M_writer(str(featured.pop(0).title()))
                        __M_writer('">\n')
                    else:
                        __M_writer('                           <div class="card-text mb-auto bootblog4-featured-text">')
                        __M_writer(str(featured.pop(0).text(teaser_only=True, strip_html=theme_config.get('featured_strip_html', True))))
                        __M_writer('</div>\n                           </div>\n')
                    __M_writer('                    </div>\n                </div>\n')
                __M_writer('       </div>\n')
            __M_writer('    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/home/nicky/.direnv/python-3.8.2/lib/python3.8/site-packages/nikola/data/themes/bootblog4/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "32": 5, "35": 6, "41": 0, "85": 2, "86": 3, "87": 4, "88": 5, "89": 6, "90": 7, "95": 15, "100": 69, "105": 146, "111": 9, "124": 9, "125": 10, "126": 10, "127": 11, "128": 12, "129": 12, "130": 12, "131": 14, "132": 14, "133": 14, "139": 17, "169": 17, "174": 20, "175": 21, "176": 22, "177": 22, "178": 22, "179": 24, "180": 25, "181": 25, "182": 25, "183": 27, "184": 28, "185": 29, "186": 29, "187": 29, "188": 31, "189": 31, "190": 31, "191": 31, "192": 34, "193": 35, "194": 35, "195": 35, "196": 35, "197": 35, "198": 36, "199": 37, "200": 37, "201": 37, "202": 39, "203": 41, "204": 41, "205": 42, "206": 42, "207": 42, "208": 42, "209": 42, "210": 42, "211": 43, "212": 44, "213": 44, "214": 44, "215": 45, "216": 45, "217": 45, "218": 45, "219": 45, "220": 45, "221": 47, "222": 49, "223": 50, "224": 50, "225": 50, "226": 52, "227": 54, "228": 55, "229": 56, "230": 56, "231": 58, "232": 59, "233": 60, "234": 60, "235": 63, "236": 65, "237": 66, "238": 66, "239": 67, "240": 67, "241": 68, "242": 68, "248": 18, "258": 18, "259": 19, "260": 19, "266": 71, "281": 71, "282": 72, "283": 73, "284": 74, "285": 75, "286": 76, "287": 78, "288": 79, "289": 82, "290": 82, "291": 82, "292": 82, "293": 83, "294": 84, "295": 84, "296": 84, "297": 86, "298": 87, "299": 88, "300": 89, "301": 91, "302": 91, "303": 91, "304": 91, "305": 91, "306": 93, "307": 94, "308": 94, "309": 94, "310": 97, "311": 100, "312": 101, "313": 102, "314": 103, "315": 104, "316": 105, "317": 106, "318": 108, "319": 111, "320": 111, "321": 111, "322": 111, "323": 113, "324": 114, "325": 114, "326": 114, "327": 116, "328": 116, "329": 116, "330": 116, "331": 117, "332": 118, "333": 118, "334": 118, "335": 121, "336": 124, "337": 125, "338": 129, "339": 129, "340": 129, "341": 129, "342": 131, "343": 132, "344": 132, "345": 132, "346": 134, "347": 134, "348": 134, "349": 134, "350": 135, "351": 136, "352": 136, "353": 136, "354": 139, "355": 142, "356": 144, "362": 356}}
__M_END_METADATA
"""
