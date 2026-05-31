import flet as ft

# main.py 상단 수정
from repository import (
    DatabaseManager,
    FridgeRepository,
    RecipeRepository,
    MappingRepository,
    JoinRepository,
)
from service import JachiService  # 추후 생성할 서비스 클래스
import views


def main(page: ft.Page):
    # region [Page Setup]
    page.title = "자취 냉장고 매니저"
    page.padding = 16
    page.window.width = 700
    page.window.height = 800
    # endregion

    # =========================================================================
    # region [의존성 주입 및 데이터베이스 초기화]
    # =========================================================================
    db_manager = DatabaseManager()

    # 각 리포지토리 인스턴스화
    fridge_repo = FridgeRepository(db_manager)
    recipe_repo = RecipeRepository(db_manager)
    mapping_repo = MappingRepository(db_manager)
    join_repo = JoinRepository(db_manager)

    # 서비스 계층에 의존성 주입
    service = JachiService(
        fridge_repo=fridge_repo,
        recipe_repo=recipe_repo,
        mapping_repo=mapping_repo,
        join_repo=join_repo,
    )
    # endregion

    # =========================================================================
    # region [뷰 생성 (각 탭 화면)]
    # =========================================================================
    # 각 탭에 필요한 데이터를 서비스에서 조회하여 전달
    tab_fridge = views.create_fridge_view(service)
    tab_recipes = views.create_recipe_view(service)
    tab_matching = views.create_matching_view(service)
    tab_settings = views.create_settings_view(service)

    # =========================================================================
    # region [Flet UI 레이아웃 구성]
    # =========================================================================
    tabs = ft.Tabs(
        length=4,
        expand=True,
        content=ft.Column(
            expand=True,
            controls=[
                ft.TabBar(
                    tabs=[
                        ft.Tab(label="내 냉장고", icon=ft.Icons.FRIDGE_OUTLINED),
                        ft.Tab(label="레시피 목록", icon=ft.Icons.MENU_BOOK_OUTLINED),
                        ft.Tab(label="해먹기 매칭", icon=ft.Icons.MATCH_CASE_OUTLINED),
                        ft.Tab(label="설정/모드", icon=ft.Icons.SETTINGS_OUTLINED),
                    ]
                ),
                ft.TabBarView(
                    expand=True,
                    controls=[
                        tab_fridge,
                        tab_recipes,
                        tab_matching,
                        tab_settings,
                    ],
                ),
            ],
        ),
    )

    page.add(tabs)


if __name__ == "__main__":
    ft.app(target=main)
