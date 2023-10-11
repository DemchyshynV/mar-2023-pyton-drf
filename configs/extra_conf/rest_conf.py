REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    'DEFAULT_PAGINATION_CLASS': 'core.pagination.PagePagination',
    # 'PAGE_SIZE': 2
}
