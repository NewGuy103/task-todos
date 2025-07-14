# Improve sorting/filtering functionality and implement categories

**Version**: v0.1.0

**Date:** 14/07/2025

## Additions

**`/app/controllers/sort_filter.py`**:

* Added UI controller for sorting/filtering options.

**`/app/models.py`**:

* Added models and enums related to sorting/filtering.
* Added `BuiltinCategories` enum.

**`/app/controllers/tasks.py`**:

* Added lots of logging calls for easier debugging.

## Changes

**`/scripts/build-post-generate.py`**:

* Removed redundant `build-post-generate.py` as `pyside6-deploy` can already rename per platform.

**`/app/controllers/tasks.py`**:

* Changed and improved `SortAndFilterController` to also handle adding data to the model.
* Moved model instance from `TasksItemsController` to `TaskTodosController`.

## Misc

* `pyside-deploy.yml` can now build binaries from the `main` branch.
* Next step is to find a way to get the app working on Android so many logging calls are required.
