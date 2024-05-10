from django.contrib import admin
from .models import Movie, Review


# Inline admin for Review model to edit reviews directly from the Movie admin page
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1  # Number of extra blank forms to show
    fields = ['user', 'text', 'rating', 'created_at']
    readonly_fields = ['created_at']  # Make created_at field read-only


# Custom action to reset IMDb ratings
def reset_imdb_ratings(modeladmin, request, queryset):
    queryset.update(imdb_rating=0)


reset_imdb_ratings.short_description = "Reset IMDb ratings for selected movies"


# Admin configuration for Movie model
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'imdb_rating', 'number_of_reviews')
    search_fields = ['title', 'imdb_id']
    list_filter = ['release_date', 'imdb_rating']
    inlines = [ReviewInline]
    actions = [reset_imdb_ratings]

    # Helper method to display the number of reviews directly in the admin list view
    def number_of_reviews(self, obj):
        return obj.reviews.count()

    number_of_reviews.short_description = 'Number of Reviews'


# Admin configuration for Review model
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('movie', 'user', 'rating', 'created_at')
    list_select_related = ['movie', 'user']  # Optimizes query performance
    search_fields = ['movie__title', 'user__username']
    list_filter = ['rating', 'created_at']


# Registering the models with their respective admin configuration
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review, ReviewAdmin)
