from __future__ import annotations

from typing import Any, NotRequired, TypedDict
from datetime import datetime
from uuid import UUID
from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ResultedFlat:
    cian_id: int
    city: str
    street: str
    lat: float
    lon: float
    price_sq: float
    area: float
    floor: int
    kitchen_area: float
    bathroom_type: str
    balconies: int
    renovation: float
    is_apartment: bool
    rooms: int
    ceiling_height: float
    house_floors: int
    house_wall_type: str
    lifts: int
    freight_lifts: int
    time_on_foot_to_subway: float
    build_year: int


class ResponseData(TypedDict):
    offer: Offer
    seoLinks: list[Any]
    breadcrumbs: list[Breadcrumb]
    similarOffersMapQs: str
    similarNewObjects: list[SimilarNewObject]
    linkToMap: str
    isFavorite: bool
    offerFoldersCount: int
    subscription: Subscription
    priceChanges: list[PriceChange]
    newObject: NewObject
    company: Company
    offences: list[Any]
    stats: Stats
    notes: Any
    agent: Agent
    specialProject: SpecialProject
    user: User
    agentAvailability: AgentAvailability
    countrysideProjects: CountrysideProjects
    isHiddenByUser: bool
    degradationInfo: DegradationInfo
    newbuildingDynamicCalltracking: NewbuildingDynamicCalltracking
    newbuildingFlatViewOrder: NewbuildingFlatViewOrder
    priceInfo: PriceInfo
    offersComparisonStatus: OffersComparisonStatus
    isOnlineRegistrationAvailable: bool
    isBookedFromDeveloper: bool
    factoids: list[Factoid]
    sidebar: list[SidebarOrMetric]
    features: list[Feature]
    seoData: SeoData
    trackingUrl: str
    amenities: list[Any]
    newbuildingRating: float
    newbuildingReliability: NewbuildingReliability
    offerPrice: str


class Offer(TypedDict):
    category: str
    status: str
    dealType: str
    offerType: str
    geo: Geo
    id: int
    objectGuid: UUID
    cianId: int
    userId: int
    publishedUserId: int
    cianUserId: int
    description: str
    photos: list[Photo]
    phones: list[Phone]
    publishTerms: PublishTerms
    flatType: str
    isApartments: bool
    totalArea: str
    livingArea: str
    kitchenArea: str
    projectDeclarationUrl: str
    decoration: str
    flags: Flags
    specialty: Specialty
    isNeedHideExactAddress: bool
    areaParts: list[Any]
    roomsCount: int
    floorNumber: int
    bargainTerms: BargainTerms
    building: Building
    editDate: datetime
    humanizedEditDate: str
    isInHiddenBase: bool
    isObjectHidden: bool
    isClosedVisibility: bool
    videos: list[Any]
    priceTotal: int
    priceTotalRur: int
    exportLinks: ExportLinks
    added: str
    categoriesIds: list[int]
    publicationDate: int
    creationDate: datetime
    recoveryLink: str
    isFromBuilder: bool
    isFromSeller: bool
    isFromLeadFactory: bool
    trackingData: TrackingData
    editPhoto: str
    newEdit: str
    certificate: str
    edit: str
    similarOffersLink: str
    similarOffersCount: int
    buildersIds: list[int]
    isImported: bool
    userConfirmedFix: bool
    newbuilding: Newbuilding
    timezone: int
    isEnabledCallTracking: bool
    isRentByParts: bool
    isDuplicate: bool
    userTrust: str
    userTrustLevel: str
    showWarningMessage: bool
    moderationInfo: ModerationInfo
    isUnique: bool
    isUniqueForCian: bool
    isUniqueCheckDate: str
    isCianPartner: bool
    externalId: str
    isIllegalConstruction: bool
    externalOfferUrl: str
    cianLayouts: None
    demolishedInMoscowProgramm: bool
    chat: bool


class Geo(TypedDict):
    address: list[Address]
    coordinates: Coordinates
    highways: list[Any]
    jk: Jk
    railways: list[Railway]
    undergrounds: list[Underground]


class Address(TypedDict):
    fullName: str
    id: int
    locationTypeId: int
    name: str
    shortName: str
    type: str
    url: str


class Coordinates(TypedDict):
    lat: float
    lng: float


class Jk(TypedDict):
    id: int
    name: str
    developer: Developer
    house: House
    gaGeo: GaGeo
    fullUrl: str
    fullUrlTemplate: str
    webSiteUrl: str


class Developer(TypedDict):
    name: str


class House(TypedDict):
    id: int
    name: str


class GaGeo(TypedDict):
    moId: int
    oblId: int
    cityId: int


class Railway(TypedDict):
    id: int
    directionIds: list[int]
    distance: str
    time: int
    name: str
    travelType: str


class Underground(TypedDict):
    id: int
    name: str
    lineColor: str
    travelType: str
    travelTime: int
    url: str
    underConstruction: bool


class Photo(TypedDict):
    id: int
    isDefault: bool
    fullUrl: str
    thumbnailUrl: str
    thumbnail2Url: str
    miniUrl: str
    isLayout: bool
    isCianLayout: bool


class Phone(TypedDict):
    countryCode: str
    number: str


class PublishTerms(TypedDict):
    terms: list[Term]
    autoprolong: bool


class Term(TypedDict):
    services: list[str]
    days: int
    type: str


class Flags(TypedDict):
    isArchived: bool
    isCommercialOwnershipVerified: bool


class Specialty(TypedDict):
    types: list[Any]
    additionalTypes: list[Any]


class BargainTerms(TypedDict):
    price: int
    priceType: str
    currency: str
    saleType: str
    includedOptions: list[Any]
    prices: Prices
    tags: list[Any]


class Prices(TypedDict):
    rur: int
    usd: int
    eur: int


class Building(TypedDict):
    materialType: str
    floorsCount: int
    ceilingHeight: str
    totalArea: str
    liftTypes: list[Any]
    cranageTypes: list[Any]
    deadline: Deadline
    houseMaterialType: str


class Deadline(TypedDict):
    year: int
    quarter: str
    isComplete: bool
    quarterEnd: str


class ExportLinks(TypedDict):
    pdfUrl: str
    docxUrl: str


class TrackingData(TypedDict):
    moId: int
    oblId: int
    cityId: int
    fbRegion: str
    fbCity: str


class Newbuilding(TypedDict):
    id: str
    name: str
    house: HouseBuilding
    isTariffPremium: bool
    isFromDeveloper: bool
    isFromBuilder: bool
    isFromSeller: bool
    isFromLeadFactory: bool
    showJkReliableFlag: bool
    isFichering: bool
    isFicheringPlus: bool
    isPremium: bool
    newbuildingFeatures: NewbuildingFeatures
    isReliable: bool



class HouseBuilding(TypedDict):
    isReliable: bool
    isFinished: bool
    finishDate: FinishDate
    id: int
    name: str


class FinishDate(TypedDict):
    quarter: int
    year: int


class NewbuildingFeatures(TypedDict):
    imagesCount: int
    firstImageUrl: str
    videosCount: int
    deadlineInfo: str


class ModerationInfo(TypedDict):
    showContactWarningMessage: bool


class Breadcrumb(TypedDict):
    url: str
    title: str


class SimilarNewObject(TypedDict):
    id: int
    photoUrl: str
    roomTitle: str
    addressStr: str
    floor: int
    floorn: int
    kitchenArea: float
    livingArea: float
    priceRur: int
    publishedUserId: int
    totalArea: float
    undergroundInfo: UndergroundInfo


class UndergroundInfo(TypedDict):
    lineColor: str
    name: str
    type: str


class Subscription(TypedDict):
    isSubscribed: bool


class PriceChange(TypedDict):
    changeTime: datetime
    priceData: PriceData


class PriceData(TypedDict):
    currency: str
    price: int


class NewObject(TypedDict):
    newbuildingFeatures: NewObjectNewbuildingFeatures
    id: int
    name: str
    url: str
    status: str
    developer: NewObjectDeveloper
    totalCountOfferInNewobject: int
    roomsInfo: list[RoomsInfo]
    hasLayoutImageOffers: bool
    fullUrlWithSubdomain: str
    advantages: list[Any]
    specifications: list[Specification]
    promoInfos: list[Any]
    decorations: list[Decoration]
    gaLabel: str
    nearbyNewbuildingsMapUrl: str
    transportAccessibilityRate: float



class NewObjectNewbuildingFeatures(TypedDict):
    imagesCount: int
    firstImageUrl: str
    videosCount: int
    reviewsCount: int
    hasProgressOfConstructions: bool



class NewObjectDeveloper(TypedDict):
    id: int
    url: str
    name: str
    logoUrl: str
    stats: NewObjectDeveloperStats


class NewObjectDeveloperStats(TypedDict):
    progress: Progress
    done: Done


class Progress(TypedDict):
    qs: str


class Done(TypedDict):
    text: str
    qs: str


class RoomsInfo(TypedDict):
    type: str
    minArea: float
    maxPrice: int
    minPrice: int
    offersCount: int
    url: str


class Specification(TypedDict):
    title: str
    value: str
    valueTooltipText: NotRequired[str]


class Decoration(TypedDict):
    description: str
    images: list[Image]
    shortDescription: str
    title: str
    type: str
    housesIds: list[int]
    searchUrl: str


class Image(TypedDict):
    thumbnailUrl: str
    url: str


class Company(TypedDict):
    buildersAuctionRank: int
    buildingStatus: list[BuildingStatu]
    categoryId: int
    description: str
    fromDeveloperPropsCount: int
    hasSpecProject: bool
    id: int
    isTest: bool
    locationIds: list[int]
    maxBet: int
    name: str
    newobjectsCount: int
    offersCount: int
    phones: list[Any]
    promoCount: int
    specProjectNewobjectsCount: int
    status: int
    website: str
    yearFoundation: int
    url: str
    isReliable: bool
    stats: CompanyStats
    headerImageUrl: str
    newbuildingIds: list[int]
    advantages: list[Any]
    workYears: WorkYears
    reviewStats: ReviewStats
    housesBuiltInTime: str
    email: None
    emailForRequest: None
    logoUrl: None


class BuildingStatu(TypedDict):
    count: int
    housesCount: int
    statusId: int



class CompanyStats(TypedDict):
    housesDone: HousesInProgressOrHousesDone
    housesInProgress: HousesInProgressOrHousesDone
    newbuildingCount: NewbuildingCountOrNewbuildingWithOffers
    newbuildingWithOffers: NewbuildingCountOrNewbuildingWithOffers


class HousesInProgressOrHousesDone(TypedDict):
    housesCount: int
    newbuildingCount: int
    qs: str


class NewbuildingCountOrNewbuildingWithOffers(TypedDict):
    qs: str
    text: str
    value: int


class WorkYears(TypedDict):
    text: str
    value: int


class ReviewStats(TypedDict):
    reviewCount: int
    reviewCountText: str
    totalRate: float



class Stats(TypedDict):
    daily: int
    total: int
    totalViewsFormattedString: str
    totalUniqueViewsFormattedString: str


class Agent(TypedDict):
    id: int
    cianUserId: int
    realtyUserId: int
    accountType: str
    companyName: str
    creationDate: datetime
    name: str
    isPro: bool
    phones: list[AgentPhone]
    skills: list[Any]
    isDeveloper: bool
    isRecidivist: bool
    isUserOffersHasErrors: bool
    offersCount: int
    offersLink: str
    availableServices: AvailableServices
    userType: str
    removeCompetitor: bool
    status: str
    isSubAgent: bool
    isMessagingEnabled: bool
    isPassportVerified: bool
    isSelfEmployed: bool
    isPrivateBroker: bool
    isCianPartner: bool
    canShowOnline: bool
    moderationInfo: AgentModerationInfo
    isHidden: bool
    metrics: list[SidebarOrMetric]
    agentlists: list[Any]



class AgentPhone(TypedDict):
    confirmed: bool


class AvailableServices(TypedDict):
    isUploadsAvailable: bool
    isCallTrackingAvailable: bool
    isPhoneChangingAvailable: bool
    isServicePackagesAvailable: bool
    canUseHiddenBase: bool



class AgentModerationInfo(TypedDict):
    isUserIdentified: bool
    isUserIdentifiedByDocuments: bool
    showUserIdentifiedByDocuments: bool


class SidebarOrMetric(TypedDict):
    title: str
    value: str


class SpecialProject(TypedDict):
    id: str
    link: str


class User(TypedDict):
    isAuthenticated: bool
    permissions: Permissions
    ga: Ga


class Permissions(TypedDict):
    canModerateUsers: bool
    canModerateAnnouncements: bool
    canModerateAnnouncementsExpert: bool
    canViewUsers: bool
    canViewAnnouncements: bool


class Ga(TypedDict):
    type: str
    balance: int
    packages: list[Any]
    emailMd5: str


class AgentAvailability(TypedDict):
    userId: int
    available: bool


class CountrysideProjects(TypedDict):
    areProjectsHidden: bool
    projects: list[Any]


class DegradationInfo(TypedDict):
    stats: bool
    isFavorite: bool
    offerFoldersCount: bool
    notes: bool
    subscription: bool
    priceChanges: bool
    user: bool
    btiData: bool
    newObject: bool
    agent: bool
    offences: bool
    businessShoppingCenter: bool
    company: bool
    agentAvailability: bool
    kp: bool
    countrysideProjects: bool
    agentReviews: bool
    isHiddenByUser: bool
    newbuildingDynamicCalltracking: bool
    tour: bool
    externalTour: bool
    houseCardEntrypointData: bool
    newbuildingFlatViewOrder: bool
    newbuildingsNearby: bool


class NewbuildingDynamicCalltracking(TypedDict):
    siteBlockId: int


class NewbuildingFlatViewOrder(TypedDict):
    isEnabled: bool
    orderStatus: OrderStatus


class OrderStatus(TypedDict):
    type: str


class PriceInfo(TypedDict):
    pricePerSquareValue: int


class OffersComparisonStatus(TypedDict):
    status: str
    description: str


class Factoid(TypedDict):
    title: str
    icon: str
    value: str



class Feature(TypedDict):
    title: str
    id: str
    features: list[FeatureValue]



class FeatureValue(TypedDict):
    value: str
    label: str


class SeoData(TypedDict):
    socialNetworksTitle: SocialNetworksTitle
    mainTitle: str
    description: str
    micromarking: Micromarking


class SocialNetworksTitle(TypedDict):
    full: str
    short: str


AuthorOrBrand = TypedDict(
    "AuthorOrBrand",
    {
        "@type": str,
        "name": str,
    },
)

ReviewRating = TypedDict(
    "ReviewRating",
    {
        "@type": str,
        "ratingValue": float,
        "bestRating": int,
    },
)

Review = TypedDict(
    "Review",
    {
        "@type": str,
        "reviewRating": ReviewRating,
        "author": AuthorOrBrand,
    },
)

Offers = TypedDict(
    "Offers",
    {
        "@type": str,
        "url": str,
        "priceCurrency": str,
        "availability": str,
        "price": int,
    },
)
Micromarking = TypedDict(
    "Micromarking",
    {
        "@context": str,
        "@type": str,
        "name": str,
        "image": list[str],
        "description": str,
        "sku": int,
        "brand": AuthorOrBrand,
        "review": Review,
        "offers": Offers,
    },
)


class NewbuildingReliability(TypedDict):
    actions: Actions
    checkStatus: CheckStatus
    details: list[Detail]


class Actions(TypedDict):
    details: str


class CheckStatus(TypedDict):
    date: str
    status: str
    title: str


class Detail(TypedDict):
    iconType: str
    title: str
    type: str
    label: NotRequired[str]
